from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
import pandas as pd

class FairnessAuditor:
    def __init__(self, protected_attribute: str = "gender"):
        self.protected_attr = protected_attribute
        
    def analyze(self, predictions: pd.DataFrame) -> dict:
        """Run full fairness audit"""
        dataset = BinaryLabelDataset(
            df=predictions,
            label_names=['score'],
            protected_attribute_names=[self.protected_attr]
        )
        
        # 1. Disparate Impact
        metric = ClassificationMetric(
            dataset, 
            dataset, 
            unprivileged_groups=[{self.protected_attr: 0}],
            privileged_groups=[{self.protected_attr: 1}]
        )
        
        # 2. Mitigation
        reweighter = Reweighing(
            unprivileged_groups=[{self.protected_attr: 0}],
            privileged_groups=[{self.protected_attr: 1}]
        )
        mitigated = reweighter.fit_transform(dataset)
        
        return {
            "disparate_impact": metric.disparate_impact(),
            "statistical_parity": metric.statistical_parity_difference(),
            "average_odds_difference": metric.average_odds_difference(),
            "mitigated_weights": mitigated.instance_weights.tolist()
        }
