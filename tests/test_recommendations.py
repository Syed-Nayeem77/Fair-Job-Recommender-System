import pytest
import numpy as np
from model.two_tower_model import TwoTowerRecommender
from sklearn.feature_extraction.text import TfidfVectorizer

@pytest.fixture
def sample_data():
    return {
        "candidates": ["python sql", "java aws", "python aws"],
        "jobs": ["data scientist python", "cloud engineer aws"]
    }

@pytest.fixture
def trained_model(sample_data):
    model = TwoTowerRecommender()
    model.train(sample_data["candidates"], sample_data["jobs"])
    return model

def test_recommendations(trained_model):
    # Test basic functionality
    recommendations = trained_model.recommend("python")
    assert len(recommendations) > 0
    assert all("job_id" in r and "score" in r for r in recommendations)

def test_model_persistence(tmp_path, trained_model):
    # Test model saving/loading
    import pickle
    model_path = tmp_path / "test_model.pkl"
    
    # Save
    with open(model_path, "wb") as f:
        pickle.dump((trained_model.candidate_vectorizer, trained_model.job_vectorizer), f)
    
    # Load
    with open(model_path, "rb") as f:
        candidate_vec, job_vec = pickle.load(f)
    
    assert hasattr(candidate_vec, "transform")  # Verify loaded components work

def test_edge_cases(trained_model):
    # Empty input
    with pytest.raises(ValueError):
        trained_model.recommend("")
    
    # Unknown skills
    results = trained_model.recommend("unknown_skill")
    assert isinstance(results, list)
