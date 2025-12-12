import requests
import streamlit as st

# URL of your FastAPI backend
BACKEND_URL = "http://localhost:8000"  # On Hugging Face, localhost is still correct inside the container

st.set_page_config(page_title="Sleep K-Means Clustering", layout="centered")
st.title("😴 Sleep K-Means Clustering")
st.write("Upload preprocessed EEG CSV files (HPC, PFC, EMG), and the app will find the best number of clusters automatically.")

st.markdown("### 1. Upload your files")

hpc_file = st.file_uploader("HPC CSV file", type=["csv"], key="hpc")
pfc_file = st.file_uploader("PFC CSV file", type=["csv"], key="pfc")
emg_file = st.file_uploader("EMG CSV file", type=["csv"], key="emg")

if st.button("Run clustering"):
    if not hpc_file or not pfc_file or not emg_file:
        st.error("Please upload all three files: HPC, PFC, and EMG.")
    else:
        with st.spinner("Running K-Means and computing silhouette scores..."):
            try:
                files = {
                    "hpc_file": (hpc_file.name, hpc_file.getvalue(), "text/csv"),
                    "pfc_file": (pfc_file.name, pfc_file.getvalue(), "text/csv"),
                    "emg_file": (emg_file.name, emg_file.getvalue(), "text/csv"),
                }

                resp = requests.post(f"{BACKEND_URL}/predict", files=files)

                if resp.status_code != 200:
                    st.error(f"API error {resp.status_code}: {resp.text}")
                else:
                    data = resp.json()
                    st.success(f"✅ Optimal number of clusters: **k = {data['optimal_k']}**")

                    st.markdown("### 2. Silhouette scores")
                    st.json(data["scores"])

                    st.markdown("### 3. First 50 cluster labels")
                    st.write(data["clusters"][:50])

            except Exception as e:
                st.error(f"Request failed: {e}")
