FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (including the pickle model)
COPY . .

# Expose ports: 8000 for FastAPI, 7860 for Streamlit UI
EXPOSE 8000
EXPOSE 7860

# Start FastAPI and Streamlit in the same container
CMD bash -c "uvicorn api:app --host 0.0.0.0 --port 8000 & \
             streamlit run app.py --server.port 7860 --server.address 0.0.0.0"
