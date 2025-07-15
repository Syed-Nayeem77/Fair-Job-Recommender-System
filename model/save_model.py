# File: model/save_model.py
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from config.settings import settings

# Initialize and train a dummy model
vectorizer = TfidfVectorizer()
vectorizer.fit(["python developer", "java engineer", "data scientist"])

# Save versioned model
model_data = {
    "model": vectorizer,
    "version": settings.MODEL_VERSION,
    "training_date": "2024-03-25",
    "metrics": {
        "sample_accuracy": 0.92,
        "training_time_sec": 42.5
    }
}

with open(settings.MODEL_PATH, "wb") as f:
    pickle.dump(model_data, f)

print(f"Model saved to: {settings.MODEL_PATH}")
