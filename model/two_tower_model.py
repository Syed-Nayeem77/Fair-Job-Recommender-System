import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import uuid

def recommend_jobs(candidate):
    # Load job listings
    job_df = pd.read_csv("data/jobs.csv")

    # Vectorize skills
    tfidf = TfidfVectorizer()
    job_vectors = tfidf.fit_transform(job_df['required_skills'])

    # Transform candidate's skills
    candidate_vector = tfidf.transform([candidate.skills])

    # Compute cosine similarity
    similarities = cosine_similarity(candidate_vector, job_vectors).flatten()

    # Attach similarity scores to jobs
    job_df['score'] = similarities

    # Get top 5 matches
    top_matches = job_df.sort_values(by="score", ascending=False).head(5)

    # Convert to list of dictionaries
    results = []
    for _, row in top_matches.iterrows():
        results.append({
            "id": str(uuid.uuid4()),
            "title": row['title'],
            "required_skills": row['required_skills'],
            "score": row['score']
        })

    return results
