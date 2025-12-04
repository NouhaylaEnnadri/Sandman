from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.signal import spectrogram

app = FastAPI(title="Sleep K-Means Automatic Clustering API")

TARGET_FS = 500
EPOCH_DURATION = 2

FREQUENCY_BANDS = {
    'delta': (0.5, 4),
    'theta': (6, 9),
    'sigma': (12, 16),
    'beta': (15, 30),
    'gamma': (30, 80)
}

BAND_ORDER = list(FREQUENCY_BANDS.keys())


def extract_spectral_features(signal, fs, bands, epoch_duration):
    nperseg = int(fs * epoch_duration)
    f, t, Sxx = spectrogram(signal, fs=fs, nperseg=nperseg, noverlap=0,
                           detrend=False, scaling='density', mode='psd')
    
    features = []
    for band_name, (low, high) in bands.items():
        mask = (f >= low) & (f <= high)
        band_power = np.trapezoid(Sxx[mask, :], f[mask], axis=0)
        features.append(band_power)
    
    return np.vstack(features).T  # shape: (epochs, n_bands)


def preprocess_features(X):
    scaler = RobustScaler()
    return scaler.fit_transform(X)


@app.post("/predict")
async def predict_clusters(
    hpc_file: UploadFile = File(...),
    pfc_file: UploadFile = File(...),
    emg_file: UploadFile = File(...)
):
    try:
        # Read CSVs
        hpc = pd.read_csv(hpc_file.file).iloc[:, 0].values
        pfc = pd.read_csv(pfc_file.file).iloc[:, 0].values
        emg = pd.read_csv(emg_file.file).iloc[:, 0].values
    except Exception:
        raise HTTPException(400, "Error reading CSV files")

    # Extract features
    hpc_feats = extract_spectral_features(hpc, TARGET_FS, FREQUENCY_BANDS, EPOCH_DURATION)
    pfc_feats = extract_spectral_features(pfc, TARGET_FS, FREQUENCY_BANDS, EPOCH_DURATION)

    # Combine
    X = np.hstack([hpc_feats, pfc_feats])
    X = preprocess_features(X)

    # Try different k values
    K_RANGE = range(2, 7)
    silhouette_scores = {}
    best_k = None
    best_score = -1

    for k in K_RANGE:
        kmeans = KMeans(n_clusters=k, n_init=20, random_state=42)
        labels = kmeans.fit_predict(X)
        score = silhouette_score(X, labels)
        silhouette_scores[k] = float(score)

        if score > best_score:
            best_score = score
            best_k = k
            best_labels = labels.tolist()

    return {
        "optimal_k": best_k,
        "scores": silhouette_scores,
        "clusters": best_labels
    }
