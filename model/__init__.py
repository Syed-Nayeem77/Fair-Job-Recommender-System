# model/__init__.py
from .two_tower_model import TwoTowerRecommender
from .fairness_check import FairnessAuditor

__all__ = ["TwoTowerRecommender", "FairnessAuditor"]
