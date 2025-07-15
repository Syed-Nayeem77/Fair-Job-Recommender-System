# Fair Job Recommender System

---

##  Key Features

| Feature               | Implementation                                  | Tools Used        |
| --------------------- | ----------------------------------------------- | ----------------- |
| Recommendation Engine | Two-tower neural network with hybrid embeddings | PyTorch, TF-IDF   |
| Explainable AI        | Real-time SHAP explanations for recommendations | SHAP, LIME        |
| Bias Detection        | Demographic parity checks on recommendations    | AIF360, Fairlearn |
| Scalable Deployment   | Containerized microservice with auto-scaling    | Docker, AWS ECS   |

---

##  Project Structure

```
.
├── api/                         # FastAPI app (Dockerized)
│   ├── main.py                  # API endpoints
│   └── Dockerfile               # Container config
├── config/                      # Centralized configs
│   └── settings.py              # Environment variables
├── model/                       # Core ML logic
│   ├── two_tower_model.py       # Neural recommender
│   └── fairness_check.py        # Bias audits
├── models/                      # Versioned model binaries
│   └── model_v1_0_0.pkl         # Serialized production model
├── monitoring/                  # Performance tracking
│   ├── drift_report.html        # Evidently reports
│   └── metrics.json             # Historical metrics
├── terraform/                   # AWS infrastructure (optional)
│   └── main.tf                  # Terraform scripts
└── assets/
    └── images/
        └── metrics.png          # Dashboard image
```

##  Quick Start

###  Installation

git clone https://github.com/Syed-Nayeem77/Fair-Job-Recommender-System.git
cd Fair-Job-Recommender-System
pip install -r requirements.txt
```

### Local Deployment (Docker)

docker build -f api/Dockerfile -t job-recommender .
docker run -p 8000:8000 job-recommender
```

### API Usage

curl -X POST http://localhost:8000/recommend \
     -H "Content-Type: application/json" \
     -d '{"skills": "python sql"}'
```

---

##  Cloud Deployment (Terraform on AWS)

cd terraform
terraform init
terraform apply -auto-approve
```

##  Performance Dashboard

**Latest Model Metrics:**

```json
{
  "accuracy": 0.92,
  "latency_ms": 45.2,
  "fairness_metrics": {
    "disparate_impact": 1.08,
    "statistical_parity": -0.03
  }
}
```

---

##  Maintenance

###  Retraining Model

python model/train.py --new-data data/candidates.csv
```

###  Monitoring & Drift Detection

python monitoring/drift_detection.py



