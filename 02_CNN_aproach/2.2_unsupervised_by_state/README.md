# NREM Substage Discovery: Optimized Clustering Pipeline

## 1. High-Dimensional Feature Extraction
The process begins by transforming raw HPC and PFC signals into a comprehensive feature matrix.
*   **Windowing**: Data is segmented into **5-second windows** with a 50% overlap (2.5s step).
*   **Temporal Features**: For both channels, the pipeline calculates **RMS**, **variance**, **skewness**, **kurtosis**, and the **Zero-Crossing Rate**.
*   **Spectral Features**: Using the Welch method, the system extracts **total power** and **relative power** across six frequency bands: Delta, Theta, Alpha, Sigma, Beta, and Gamma.
*   **Advanced Metrics**: The pipeline computes **cross-correlation** between the HPC and PFC, as well as specific ratios like **Delta/Theta** and **Delta/Beta** to capture physiological signatures.

## 2. Preprocessing and Optimized Dimensionality Reduction
To prepare the 44 extracted features for clustering, the data undergoes a two-step reduction process.
*   **Enhanced PCA**: The pipeline utilizes **15 principal components** (increased from 10) to retain more detail, capturing approximately **93.41% of the variance**.
*   **Fine-Grained UMAP**: UMAP is configured with `n_neighbors=5` and `min_dist=0.0` to specifically focus on **small, local structures** and create more compact clusters.

## 3. Hierarchical Structural Analysis (Dendrogram)
Before applying flat clustering, the pipeline performs a hierarchical analysis to understand the "natural" structure of the data.
*   **Ward Linkage**: The system computes a linkage matrix and visualizes a **dendrogram** (both full and truncated) to identify distance jumps between potential clusters.
*   **Automated Suggestion**: A suggestion for the number of clusters is generated based on the largest distance jump in the hierarchy.

## 4. Clustering Optimization and Mixed Scoring
The pipeline compares two distinct clustering philosophies:
*   **Agglomerative Clustering**: The system tests a range of $K$ (2 to 10) and evaluates them using **Silhouette**, **Davies-Bouldin**, and **Calinski-Harabasz** scores.
*   **HDBSCAN with Mixed Scoring**: A grid search is performed over `min_cluster_size` and `min_samples`. A unique **"Mixed Score"** is used to select the best parameters by balancing:
    1.  **Silhouette Score** (Quality).
    2.  **Cluster Penalty** (How close the result is to the target of 5 clusters).
    3.  **Noise Ratio** (Penalizing configurations with >40-50% noise).

## 5. Visual Validation and Final Recommendation
The final step involves a side-by-side comparison of the best-performing models.
*   **UMAP Visualization**: The results of the optimal HDBSCAN and Agglomerative models are plotted in 2D space to verify cluster separation and density.
*   **Deployment Recommendation**: Based on the metrics (e.g., a Silhouette score of 0.548 for $K=2$), the pipeline provides a final recommendation on which model to use for a **controlled discovery** of NREM substages.
