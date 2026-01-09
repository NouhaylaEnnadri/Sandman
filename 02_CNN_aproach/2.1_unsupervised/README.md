# Unsupervised Brain State Discovery: ConvAE + DBSCAN Clustering

This part of the pipeline focuses on **unsupervised feature extraction** and **clustering**. By using a Convolutional Autoencoder, we compress complex spectrograms into a low-dimensional "latent space" where similar brain states naturally group together.

## 1. Environment and Parameter Setup
The process begins by defining the core parameters for signal processing and deep learning:
*   **Data Inputs**: Loading three channels: **PFC**, **HPC**, and **EMG**.
*   **Signal Specs**: Sampling rate is set to **256 Hz**, with windows of **5.0 seconds** and a **50% overlap** (2.5s step).
*   **Reproducibility**: Global seeds are set for `torch`, `numpy`, and `random` to ensure consistent results across runs.

## 2. Signal Loading and Preprocessing
*   **Loading**: Data is imported from CSV files using a custom loader.
*   **Alignment**: The three signals (PFC, HPC, EMG) are truncated to the same minimum length and stacked into a single multi-channel array.
*   **Windowing**: The continuous signals are divided into discrete windows. For example, a dataset of ~1.3 million samples results in **2,096 windows**.

## 3. Spectrogram Transformation
Instead of analyzing raw waveforms, the pipeline converts each window into a **multi-channel spectrogram** using the Short-Time Fourier Transform (STFT).
*   **Frequency Range**: Limited to **0–125 Hz**.
*   **Normalization**: A log-scale transformation is applied to the spectrograms to improve the stability of the neural network.
*   **Output**: Each window becomes a "spectral image" of shape `(3 channels, 126 frequency bins, 17 time bins)`.

## 4. Convolutional Autoencoder (CAE) Training
The heart of the unsupervised method is the **Convolutional Autoencoder**, designed to learn a compressed representation of the spectrograms.
*   **Encoder**: Uses three convolutional layers to reduce the spectral images into a **32-dimensional latent vector (Z)**.
*   **Decoder**: Uses transpose convolutional layers to reconstruct the original spectrogram from the latent vector.
*   **Training**: The model is trained for **15 epochs** using Mean Squared Error (MSE) loss, forcing the network to capture the most important features of the brain activity to succeed at reconstruction.

## 5. Dimensionality Reduction and Clustering
Once the CAE is trained, the 32-dimensional latent vectors are processed to identify distinct states:
*   **PCA**: Applied to the latent space to retain the top 50 components.
*   **DBSCAN**: An unsupervised clustering algorithm identifies dense groups in the data without needing to know the number of clusters in advance.
*   **UMAP/t-SNE**: The high-dimensional data is projected into **2D space** for visualization, with points colored by their DBSCAN cluster assignment.

## 6. Validation and Metadata Export
The final steps involve inspecting the clusters to understand what biological states they represent:
*   **Cluster Inspection**: A function allows for plotting example spectrograms from specific clusters to visually verify their characteristics.
*   **Manual Comparison**: If manual labels are available, they are overlaid on the unsupervised clusters to check for alignment between the CNN-predicted states and the discovered clusters.
*   **Metadata Export**: All results (window indices, start/end samples, and cluster IDs) are saved into a metadata dataframe for further analysis.
