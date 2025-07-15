# monitoring/drift.py
from evidently.report import Report
from evidently.metrics import DataDriftTable

def check_drift(current_data, reference_data):
    report = Report(metrics=[DataDriftTable()])
    report.run(current_data, reference_data)
    report.save_html("monitoring/drift_report.html")
