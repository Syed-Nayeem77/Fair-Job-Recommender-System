from fastapi import FastAPI
from pydantic import BaseModel
from model.two_tower_model import recommend_jobs
from model.explain_model import explain_candidate_skills
from model.fairness_check import check_fairness

app = FastAPI()

class Candidate(BaseModel):
    id: int
    name: str
    skills: str
    gender: str

class Job(BaseModel):
    id: str
    title: str
    required_skills: str

@app.get("/")
def root():
    return {"message": "Fair Job Recommender API is up and running!"}

@app.post("/recommend")
def get_recommendations(candidate: Candidate):
    try:
        return recommend_jobs(candidate)
    except Exception as e:
        return {"error": str(e)}

@app.post("/explain")
def explain_recommendation(candidate: Candidate, job: Job):
    try:
        shap_values, features = explain_candidate_skills(candidate.model_dump(), job.model_dump())
        return {
            "features": features.tolist(),
            "shap_values": shap_values.values.tolist()
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/fairness")
def fairness_analysis(job_id: int):
    try:
        result = check_fairness(job_id)
        return result
    except Exception as e:
        return {"error": str(e)}
