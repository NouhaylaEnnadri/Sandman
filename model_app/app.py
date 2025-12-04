import requests
import streamlit as st

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Sleep K-Means Clustering", layout="wide")
st.title("😴 Sleep K-Means Clustering Viewer")

st.write(
    "This app shows the K-Means cluster assigned to each 2s epoch of the preprocessed EEG."
)

# Load all clusters
if st.button("Load all clusters"):
    try:
        resp = requests.get(f"{BACKEND_URL}/clusters")
        data = resp.json()
        st.write(f"Number of epochs: {data['n_epochs']}")
        st.line_chart(data["clusters"])
    except Exception as e:
        st.error(f"Error contacting API: {e}")

st.markdown("---")

epoch_id = st.number_input("Epoch index", min_value=0, step=1, value=0)

if st.button("Get cluster for this epoch"):
    try:
        resp = requests.get(f"{BACKEND_URL}/cluster/{epoch_id}")
        if resp.status_code != 200:
            st.error(resp.text)
        else:
            data = resp.json()
            st.success(f"Epoch {data['epoch_id']} is in cluster {data['cluster']}")
    except Exception as e:
        st.error(f"Error contacting API: {e}")
