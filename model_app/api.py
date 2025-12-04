from fastapi import FastAPI, HTTPException
from sleep_model_utils import sleep_model

app = FastAPI(title="Sleep K-Means Clustering API")


@app.get("/")
def root():
    return {
        "message": "Sleep clustering API running",
        "n_epochs": sleep_model.get_num_epochs(),
        "endpoints": ["/clusters", "/cluster/{epoch_id}"],
    }


@app.get("/clusters")
def get_all_clusters():
    return {
        "n_epochs": sleep_model.get_num_epochs(),
        "clusters": sleep_model.get_all_clusters(),
    }


@app.get("/cluster/{epoch_id}")
def get_cluster(epoch_id: int):
    n = sleep_model.get_num_epochs()
    if epoch_id < 0 or epoch_id >= n:
        raise HTTPException(status_code=400, detail=f"epoch_id must be in [0, {n-1}]")
    cluster = sleep_model.get_cluster_for_epoch(epoch_id)
    return {
        "epoch_id": epoch_id,
        "cluster": cluster,
    }
