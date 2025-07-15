from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics import *

class DriftMonitor:
    def check_drift(self, current_data, reference_data):
        report = Report(metrics=[
            DataDriftTable(),
            DatasetDriftMetric()
        ])
        report.run(current_data, reference_data)
        return report.as_dict()
