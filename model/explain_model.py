import shap
import numpy as np
from sklearn.pipeline import Pipeline

class RecommendationExplainer:
    def __init__(self, model: Pipeline):
        self.model = model
        self.explainer = shap.Explainer(model.named_steps['clf'])
        
    def explain(self, candidate: dict, job_desc: str) -> dict:
        """Generate SHAP explanations for a recommendation"""
        # Preprocess input
        X = self.model.named_steps['preprocessor'].transform([candidate])
        
        # SHAP values
        shap_values = self.explainer.shap_values(X)
        
        # Feature names
        features = self.model.named_steps['preprocessor'].get_feature_names_out()
        
        return {
            "shap_values": shap_values[0].tolist(),
            "feature_names": features.tolist(),
            "base_value": float(self.explainer.expected_value),
            "sample_prediction": float(self.model.predict_proba(X)[0][1])
        }
