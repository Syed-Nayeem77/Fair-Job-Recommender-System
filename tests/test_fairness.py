import pytest
import pandas as pd
from model.fairness_check import FairnessAuditor

@pytest.fixture
def sample_predictions():
    return pd.DataFrame({
        "gender": [0, 0, 1, 1],  # 0=Female, 1=Male
        "age": [25, 30, 25, 30],
        "score": [0.2, 0.8, 0.9, 0.3]  # Recommendation scores
    })

def test_fairness_metrics(sample_predictions):
    auditor = FairnessAuditor(protected_attribute="gender")
    report = auditor.analyze(sample_predictions)
    
    # Key metrics exist
    assert "disparate_impact" in report
    assert "statistical_parity" in report
    assert "average_odds_difference" in report
    
    # Validate metric ranges
    assert 0 <= report["disparate_impact"] <= 2
    assert -1 <= report["statistical_parity"] <= 1

def test_bias_mitigation(sample_predictions):
    auditor = FairnessAuditor(protected_attribute="age")
    report = auditor.analyze(sample_predictions)
    
    # Weights should change after mitigation
    original_weights = [1.0] * len(sample_predictions)
    assert report["mitigated_weights"] != original_weights

def test_protected_attribute_handling():
    with pytest.raises(ValueError):
        # Invalid protected attribute
        FairnessAuditor(protected_attribute="invalid_attr")
