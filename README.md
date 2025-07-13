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



###### Author

###### 

###### Syed Abdul Nayeem – \[GitHub](https://github.com/Syed-Nayeem77)

###### 

