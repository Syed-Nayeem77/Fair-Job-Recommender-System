import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

MODEL_VERSION = "1.0.0"
MODEL_PATH = Path(__file__).parent.parent / "models" / f"two_tower_v{MODEL_VERSION.replace('.', '_')}.pkl"

class TwoTowerRecommender:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model_path = MODEL_PATH

    def train(self, data: list[str]):
        self.vectorizer.fit(data)
        self._save_model()

    def _save_model(self):
        """Serialize model with version metadata"""
        MODEL_PATH.parent.mkdir(exist_ok=True)
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({
                "vectorizer": self.vectorizer,
                "version": MODEL_VERSION,
                "created_at": datetime.datetime.now().isoformat()
            }, f)
