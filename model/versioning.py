# model/versioning.py
from datetime import datetime
import pickle

def save_model(model, version: str):
    path = f"models/model_v{version.replace('.', '_')}.pkl"
    with open(path, "wb") as f:
        pickle.dump({
            "model": model,
            "version": version,
            "timestamp": datetime.now().isoformat()
        }, f)
