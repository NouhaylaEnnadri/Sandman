# Unsupervised approach of Brain States

This project implements multiple unsupervised machine learning architectures to identify hidden patterns in brain activity and muscle tone. The workflow processes three primary signals: **EMG1.csv**, **HPC1.csv**, and **PFC1.csv**.

## 1. K-Means: Geometric 3D Clustering
This method groups data points based on their spatial proximity in the feature space.
*   **Preprocessing**: Signals are combined and normalized using **StandardScaler** to ensure equal weighting across channels.
*   **Algorithm**: **K-Means** is applied with $k=6$ clusters.
*   **Visualization**: A **3D scatter plot** represents the clusters along the EMG, HPC, and PFC axes, allowing for a direct spatial interpretation of different physiological states.

## 2. Restricted Boltzmann Machines (RBM) & Hybrid Pipelines
RBMs are used as stochastic neural networks for complex feature extraction.
*   **Requirement**: Data must be scaled between 0 and 1 using **MinMaxScaler**, as the BernoulliRBM processes probabilistic inputs.
*   **Feature Extraction**: The model is trained with 20 iterations to capture latent structures, reducing data to either 2 components for direct visualization or 16 components for advanced pipelines.
*   **Hybrid Approach**: A sophisticated pipeline combines **RBM features** (16 components) with **t-SNE** for 2D projection and **K-Means** for final cluster assignment, resulting in cleaner state separation than raw data alone.

## 3. Density-Based Clustering: DBSCAN & HDBSCAN
These methods identify clusters of varying shapes based on point density and can isolate noise.
*   **DBSCAN**: Uses parameters like `eps` and `min_samples` to find dense groups. It treats isolated points as **noise (label -1)**.
*   **Optimization**: The pipeline tests a range of `eps` values to determine the stability of the found clusters.
*   **HDBSCAN**: A hierarchical version that automatically identifies clusters of different densities. In the source tests, it identified **183 distinct clusters** and 1,061 noise points, offering a highly granular view of signal fluctuations.

## 4. t-SNE: Non-Linear Dimensionality Reduction
t-SNE is used to project high-dimensional brain data into a 2D "map" for human inspection.
*   **Configuration**: The model uses a low **perplexity (e.g., 3)** to focus on local structures during the 2D embedding process.
*   **Clustering on Map**: After the 2D transformation, **K-Means ($k=6$)** is applied directly to the t-SNE coordinates, effectively separating the visual "clouds" of data into distinct categories.

## 5. Gaussian Mixture Models (GMM): Probabilistic Assignment
GMM assumes that the data is composed of several Gaussian distributions, each representing a different state.
*   **Modeling**: The pipeline uses 6 components with **full covariance matrices**, allowing the clusters to take flexible, elliptical shapes.
*   **Insights**: The model provides **weights and means** for each component across all three signals, helping to define the biological profile of each discovered cluster.
*   **Temporal Mapping**: Predicted labels are plotted against the original signal time-series, visualizing how the brain transitions between these unsupervised states over time.

---

** calculates the probability that a book belongs to a certain genre, acknowledging that some books might be 70% "History" and 30% "Biography."
