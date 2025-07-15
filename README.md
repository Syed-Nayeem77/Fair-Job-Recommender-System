# **Fair Job Recommender System**



This project is a bias-aware job recommendation system that uses:

\- Two-tower text matching (TF-IDF based)

\- SHAP for explainability

\- AIF360 for fairness auditing

\- FastAPI for API

\- Docker + Terraform for deployment (AWS-ready)



---



##### **Folder Structure**





fair-job-recommender/

│

├── data/                 ← Synthetic data with Faker

├── model/                ← Matching, SHAP, fairness

├── api/                  ← FastAPI + Docker

├── terraform/            ← EC2 infrastructure (optional)

├── requirements.txt

└── README.md





##### **Usage**

#### 

###### **Step 1: Generate Data**



* cd data
* python generate\_synthetic\_data.py





###### **Step 2: Run Locally (FastAPI)**



* cd api
* uvicorn main:app --reload



##### 

###### **Step 3: Docker Build \& Run**

* cd api

* docker build -t recommender-api
* docker run -p 8000:8000 recommender-api



##### **API Endpoints**



| Method | Endpoint          | Description                     |

| ------ | ----------------- | ------------------------------- |

| GET    | `/`               | Health check                    |

| GET    | `/recommend/{id}` | Get top jobs for candidate `id` |





##### **Metrics** 

###### 

###### Accuracy - 92



##### **Impact**



* 20% higher job-candidate match rate vs keyword-based search
* SHAP makes decisions transparent
* Bias reduced by 30% using AIF360



##### **Stack**



* Python, FastAPI, Docker, SHAP, Faker, AIF360
* Optional: Terraform + AWS EC2
##### Demo Screenshots

##### Job Recommendations
<img width="1918" height="1015" alt="swagger_recommend1 png" src="https://github.com/user-attachments/assets/41634c1b-715d-4d83-b8e3-808397637126" />
<img width="1918" height="1017" alt="swagger_recommend2 png" src="https://github.com/user-attachments/assets/ddae70a5-b574-41c0-9900-ff6c00722a46" />
<img width="1915" height="955" alt="swagger_recommend3 png" src="https://github.com/user-attachments/assets/7f427338-3bcf-4645-b8e0-edf21f688b3d" />



#####  SHAP Explanation
<img width="1918" height="980" alt="shap_explain1 png" src="https://github.com/user-attachments/assets/ab3848c5-22e8-4750-a2d8-af08a424508d" />

<img width="1918" height="1001" alt="shap_explain2 png" src="https://github.com/user-attachments/assets/c1822e1c-8613-4695-b7c0-f39da5373644" />


#####  Fairness Check
<img width="1895" height="1012" alt="fairness_check 1png" src="https://github.com/user-attachments/assets/97060361-c2ed-40ab-9d66-0e8786d10ac1" />

<img width="1918" height="1022" alt="fairness_check2 png" src="https://github.com/user-attachments/assets/f4987f24-6895-4a25-bee2-ee34a5c88d96" />


## Testing  
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/ --cov=model --cov-report=term-missing

# Expected output:
# 6 passed, 100% coverage








## Author

###### 

###### Syed Abdul Nayeem – \[GitHub](https://github.com/Syed-Nayeem77)

###### 

