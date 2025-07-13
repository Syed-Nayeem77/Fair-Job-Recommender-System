import shap
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def explain_candidate_skills(candidate_profile, job_profile):
    job_df = pd.DataFrame([job_profile])  # this is correct

    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(job_df['required_skills'])
    y = job_df.get('label', [1]*len(job_df))

    model = LogisticRegression().fit(X, y)

    explainer = shap.Explainer(model, X)
    candidate_vector = tfidf.transform([candidate_profile['skills']])
    shap_values = explainer(candidate_vector)

    return shap_values, tfidf.get_feature_names_out()
