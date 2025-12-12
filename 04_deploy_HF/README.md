# How to Run Locally

### **1️ Install dependencies**

```bash
pip install -r requirements.txt
```

---

### **2️ Start the FastAPI backend**

From inside the `model_app/` folder:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

Then open:

👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

This page lets you test the `/predict` endpoint.

---

### **3️ Start the Streamlit UI**

In a **second terminal**, still inside `model_app/`:

```bash
streamlit run app.py --server.port 8501
```

Then open:

👉 **[http://localhost:8501](http://localhost:8501)**

Upload your EEG CSV files to get the **optimal number of clusters**.
