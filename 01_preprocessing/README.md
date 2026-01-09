# Brain Signals Preprocessing

**HPC & PFC Signals (MAT → ML/DL Ready Pipelines)**

The pipeline handles:

* Loading and parsing `.mat` files
* Signal cleaning and normalization
* Segmentation and feature preparation
* Computation of EMG signal


---

## Data Description

* **HPC signal**: Hippocampal brain activity recordings
* **PFC signal**: Prefrontal cortex brain activity recordings

Each signal is processed independently, then can be combined or compared depending on the downstream task (classification, regression, pattern detection, etc.).

---

## Preprocessing Pipeline

The preprocessing steps include:

1. **Loading `.mat` files**

   * Extraction of raw signal arrays
   * Verification of dimensions and sampling consistency

2. **Signal Cleaning**

   * Removal of NaNs / invalid values
   * Optional filtering (e.g. noise reduction, smoothing)

3. **Normalization**

   * Standardization (z-score) or min-max scaling
   * Ensures comparable scales between HPC and PFC

4. **Segmentation / Windowing**

   * Splitting continuous signals into fixed-size windows
   * Suitable for temporal models (CNN, RNN, Transformers, etc.)

5. **Feature Preparation**

   * Either:

     * Raw windows for Deep Learning
     * Or extracted features (statistical, spectral, etc.) for classical ML

6. **Dataset Structuring**

   * Formatting into `(X, y)` arrays
   * Ready for:

     * `scikit-learn`
     * `PyTorch`
     * `TensorFlow/Keras`

