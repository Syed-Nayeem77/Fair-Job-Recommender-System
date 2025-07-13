# data/generate_synthetic_data.py

from faker import Faker
import pandas as pd
import random

fake = Faker()
skills_list = ["Python", "SQL", "ML", "Data Science", "AWS", "Docker", "NLP", "Java", "Deep Learning", "Spark"]

def generate_jobs(n=100):
    jobs = []
    for _ in range(n):
        jobs.append({
            "id": fake.uuid4(),
            "title": fake.job(),
            "required_skills": ', '.join(fake.words(nb=random.randint(3, 6), ext_word_list=skills_list))
        })
    return pd.DataFrame(jobs)

def generate_candidates(n=20):
    candidates = []
    for _ in range(n):
        candidates.append({
            "id": fake.uuid4(),
            "name": fake.name(),
            "gender": random.choice(["Male", "Female"]),
            "skills": ', '.join(fake.words(nb=random.randint(3, 6), ext_word_list=skills_list))
        })
    return pd.DataFrame(candidates)

if __name__ == "__main__":
    generate_jobs().to_csv("../data/jobs.csv", index=False)
    generate_candidates().to_csv("../data/candidates.csv", index=False)

