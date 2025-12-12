import joblib
from typing import List, Dict


class SleepKMeansModel:
    def __init__(self, kmeans, pca, feature_names, clusters, state_mapping=None):
        self.kmeans = kmeans
        self.pca = pca
        self.feature_names = feature_names
        self.clusters = clusters
        self.state_mapping = state_mapping or {}

    def get_num_epochs(self) -> int:
        return len(self.clusters)

    def get_cluster_for_epoch(self, idx: int) -> int:
        return int(self.clusters[idx])

    def get_all_clusters(self) -> List[int]:
        return [int(c) for c in self.clusters]


def load_sleep_model(path: str = "sleep_kmeans.pkl") -> SleepKMeansModel:
    pack = joblib.load(path)
    return SleepKMeansModel(
        kmeans=pack["kmeans"],
        pca=pack["pca"],
        feature_names=pack["feature_names"],
        clusters=pack["clusters"],
        state_mapping=pack.get("state_mapping", None),
    )


# load once at import
sleep_model = load_sleep_model()
