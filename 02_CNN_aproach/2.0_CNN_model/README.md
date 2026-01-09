# Hybrid Brain State Classification: Supervised CNN & Unsupervised Pipeline

Implementation of a multi-stage pipeline for classifying sleep/wake states from electrophysiological signals (HPC and PFC). It combines a **supervised Deep Learning approach** (1D-CNN) with an **inference framework** designed to support hybrid supervised/unsupervised methodologies.

## 1. Supervised Training Phase
The first part of the workflow focuses on building a robust classifier using manually labeled data.

*   **Data Aggregation**: The pipeline loads multiple sessions (`dataset_500Hz_1.csv` through `dataset_500Hz_5.csv`) to ensure the model generalizes across different recordings.
*   **Windowing and Reshaping**: Signals from the Hippocampus (HPC) and Prefrontal Cortex (PFC) are segmented into **1-second windows** (500 samples each). The data is reshaped into a 3D tensor `(samples, 500, 2)` to be compatible with Convolutional Neural Networks.
*   **Label Encoding**: Biological labels (0, 1, 3, 4, 5) are encoded into numerical indices (0-4) to facilitate multi-class classification.
*   **CNN Architecture**: A deep 1D-CNN is constructed with three main blocks:
    *   **Feature Extraction**: Three layers of `Conv1D` with increasing filters (16, 32, 64), stabilized by **BatchNormalization** and downsampled via **MaxPooling1D**.
    *   **Classification**: A `Flatten` layer followed by a `Dense` hidden layer with **Dropout (0.5)** to prevent overfitting, ending in a `Softmax` output for the 5 classes.
*   **Training and Validation**: The model is trained over 20 epochs using the **Adam optimizer** and **Sparse Categorical Crossentropy**. A `ModelCheckpoint` ensures that only the version with the lowest validation loss is saved (`meilleur_cnn_cerveau.keras`).

## 2. Model Evaluation
Before deployment, the model's performance is rigorously tested.
*   **Performance Metrics**: Generation of a classification report showing high precision and recall for major states like Wake (1) and NREM (3).
*   **Hypnogram Comparison**: Visual validation by overlaying the "True" manual labels against the "Predicted" CNN labels over time to identify transition accuracy.

## 3. Hybrid Pipeline & Inference
The second file shifts toward a **hybrid strategy**, where the trained CNN is used to facilitate unsupervised or semi-supervised analysis.

*   **Model Loading and Mapping**: The best-performing model is reloaded. A `MAPPING_LABELS` dictionary is defined to translate the CNN's internal indices back into biologically relevant labels (e.g., translating index 2 back to Label 3/NREM).
*   **Inference on Unlabeled Data**: The pipeline processes new datasets where manual labels may be missing or ignored. The CNN provides a "first pass" classification at 1Hz (per second).
*   **Temporal Expansion**: Predicted labels are expanded back to the original **500 Hz resolution** to match the raw signal length exactly.
*   **Visualization with Behavioral Context**: A custom visualization tool generates dual-plot graphs (HPC/PFC) with background colors representing predicted states (Wake: Gold, NREM: Blue, REM: Green, etc.).

## 4. Export and Hybrid Integration
*   **Data Export**: The final processed signals, along with their **CNN-predicted states**, are exported to a new CSV file (`dataset_predicted.csv`).
*   **Hybrid Goal**: By providing a high-confidence supervised label as a baseline, this output is ready for **unsupervised refinement** (e.g., clustering within specific states to find "sub-states" or using the CNN predictions to guide unsupervised feature extraction).
