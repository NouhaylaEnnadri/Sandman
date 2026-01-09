# CNN approach overview: Hybrid Sleep-Wake Classification & Discovery

### 1. Supervised Learning: 1D-CNN Model Training
**Source:** *vertopal.com_2.0a_training_model.pdf*
The first stage involves training a **Deep 1D-Convolutional Neural Network (CNN)** to replicate manual scoring.
*   **Data Input:** Dual-channel signals (HPC and PFC) sampled at **500 Hz**, segmented into 1-second windows.
*   **Architecture:** A 3-block convolutional structure utilizing **BatchNormalization** and **Dropout** to classify five states: Wake (1), NREM (3), Intermediate (4), REM (5), and Other/Artifact (0).
*   **Performance:** The model achieves an **accuracy of 86%**, with particularly high recall for the NREM state (0.96).

### 2. Model Inference & Dataset Integration
**Source:** *vertopal.com_2.0b_use_of_model.pdf*
This stage focuses on applying the trained model to new, unlabeled datasets to create a baseline for further analysis.
*   **Reverse Mapping:** The CNN’s internal indices (0-4) are mapped back to biological labels (0, 1, 3, 4, 5).
*   **Temporal Expansion:** Predictions generated at 1 Hz are expanded to match the original **500 Hz resolution** for precise signal alignment.
*   **Data Export:** The output is a synchronized CSV (`dataset_predicted.csv`) containing raw signals and their predicted states, which serves as the entry point for unsupervised analysis.

### 3. Unsupervised Feature Extraction (ConvAE)
**Source:** *vertopal.com_2.1a_CNN_DBSCAN.pdf*
To find patterns without manual labels, the pipeline employs a **Convolutional Autoencoder (CAE)**.
*   **Spectral Analysis:** Raw signals (PFC, HPC, EMG) are converted into **multi-channel spectrograms** (0–125 Hz).
*   **Compression:** The CAE compresses these spectrograms into a **32-dimensional latent space**, capturing essential brain activity features in a reduced format.
*   **Clustering:** **DBSCAN** and **UMAP** are used on this latent space to identify dense clusters of activity, which can then be compared against manual or CNN-predicted states.

### 4. Granular NREM Substage Discovery
**Source:** *vertopal.com_2.2a_NREM_HDBSCAN4K.pdf*
The final component focuses exclusively on the NREM state (State 3) to identify **4 to 7 granular substages**.
*   **Advanced Feature Matrix:** Extraction of **44 specific features**, including temporal metrics (RMS, Skewness), spectral power bands (Delta, Sigma, etc.), and HPC-PFC cross-correlation.
*   **Optimized Clustering:**
    *   **PCA:** Reduced to 15 components to retain 93.4% variance.
    *   **Evaluation:** Comparison between **HDBSCAN** (using a mixed score for quality and noise) and **Agglomerative Clustering**.
*   **Result:** The pipeline recommends **Agglomerative Clustering** for a controlled discovery of substages, providing a hierarchical view (Dendrogram) of NREM structure.
