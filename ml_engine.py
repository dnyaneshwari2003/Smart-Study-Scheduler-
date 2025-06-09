# ml_engine.py
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import numpy as np

def predict_study_hours(grades, priorities):
    # Simple weighted formula with regression
    X = np.array([[g, p] for g, p in zip(grades, priorities)])
    y = [10 - g/10 + p for g, p in zip(grades, priorities)]  # more hours for lower grade
    model = LinearRegression().fit(X, y)
    return model.predict(X)

def cluster_subjects(subjects, grades):
    grades = np.array(grades).reshape(-1, 1)
    kmeans = KMeans(n_clusters=2, random_state=42)
    clusters = kmeans.fit_predict(grades)
    clustered = {}
    for i, cluster_id in enumerate(clusters):
        clustered.setdefault(cluster_id, []).append(subjects[i])
    return clustered
