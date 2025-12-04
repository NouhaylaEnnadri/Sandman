from fastapi import FastAPI
from sleep_model_utils import sleep_model

app = FastAPI(title="Sleep K-Means Clustering API")

@app.get("/")
def info():
    clusters = sleep_model.get_all_clusters()
    unique_clusters = sorted(set(clusters))
    n_clusters = len(unique_clusters)

    return {
        "message": "Sleep K-Means clustering model",
        "n_clusters": n_clusters,
        "clusters_available": unique_clusters,
        "endpoints": {
            "/clusters": "Get all cluster labels",
            "/cluster/{epoch_id}": "Get cluster for a specific epoch"
        }
    }
