import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

class TwoTowerRecommender:
    def __init__(self):
        self.candidate_vectorizer = TfidfVectorizer()
        self.job_vectorizer = TfidfVectorizer()
        self.model_path = Path("models/two_tower.pkl")
        
    def train(self, candidates: list[str], jobs: list[str]):
        """Train TF-IDF embeddings (replace with neural net later)"""
        self.candidate_embeddings = self.candidate_vectorizer.fit_transform(candidates)
        self.job_embeddings = self.job_vectorizer.fit_transform(jobs)
        self._save_model()
    
    def recommend(self, candidate_skills: str, top_k: int = 5) -> list[dict]:
        """Generate recommendations with similarity scores"""
        candidate_vec = self.candidate_vectorizer.transform([candidate_skills])
        sim_scores = cosine_similarity(candidate_vec, self.job_embeddings)
        top_indices = sim_scores.argsort()[0][-top_k:][::-1]
        return [{"job_id": i, "score": float(sim_scores[0][i])} for i in top_indices]
    
    def _save_model(self):
        """Persist model for API use"""
        self.model_path.parent.mkdir(exist_ok=True)
        with open(self.model_path, "wb") as f:
            pickle.dump((self.candidate_vectorizer, self.job_vectorizer), f)
