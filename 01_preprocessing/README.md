# Brain Signals Preprocessing
# EEG signal preprocessing and EMG derivation (Buzsaki Method)

This repository contains a comprehensive pipeline for processing 2 signal: signals from the **Hippocampus (HPC)** and **Prefrontal Cortex (PFC)**. The workflow ensures data integrity through artifact removal and synchronization before deriving a synthetic EMG signal for sleep-state analysis.

## Pipeline Overview

### 1. Data Acquisition and Initial Inspection
The process begins by loading raw LFP data from `.mat` files for both the HPC (Channel 46) and PFC (Channel 11), alongside a manual sleep-state classification file. 
*   **Initial state**: Signals are sampled at **2500 Hz**.
*   **Manual Scoring**: The classification data is initially recorded second-by-second.

### 2. Intelligent Artifact Removal
To ensure the quality of subsequent analyses, a custom artifact detection algorithm is applied to the raw signals.
*   **Detection Logic**: The system identifies artifacts based on two criteria:
    1.  **Amplitude**: Z-scored signal values exceeding a specific threshold (e.g., 6 or 7 standard deviations).
    2.  **Velocity**: Rapid fluctuations detected via the derivative of the z-scored signal.
*   **Consolidation**: Detected noise points are expanded by a safety window (`time_win_thresh`) and consolidated into intervals.
*   **Mitigation**: Identified artifact segments are set to zero to prevent them from skewing the results.

### 3. Signal Resampling (Downsampling)
To reduce computational load while preserving relevant physiological information, the signals are downsampled from **2500 Hz to 500 Hz**.
*   **Method**: The pipeline uses `resample_poly`, which incorporates an internal **anti-aliasing filter** to prevent high-frequency noise from folding into the lower frequency bands.
*   **Verification**: Visual comparisons are generated to ensure the downsampled signal maintains the morphology of the original LFP.

### 4. Synchronization with Manual Classification
The manual classification states (Wake, NREM, REM, etc.) are synchronized with the 500 Hz LFP signals.
*   **Upsampling Labels**: The second-by-second manual scores are repeated to match the 500 Hz sampling rate of the processed LFP.
*   **Visualization**: A custom plotting function overlays the behavioral states as colored backgrounds behind the LFP traces, allowing for direct verification of signal characteristics (like spindles or theta waves) against the scored states.

### 5. Synthetic EMG Computation (Buzsaki Method)
A critical step in sleep research is determining muscle tone (EMG). In the absence of a dedicated EMG lead, a synthetic EMG is derived from the HPC and PFC LFP signals using the **Buzsaki Method**.
*   **High-Frequency Filtering**: Both signals are filtered in a high-frequency band (**275–600 Hz**). This removes low-frequency physiological correlations (like Theta or Delta) and isolates the high-frequency "noise" that correlates with muscle activity.
*   **Correlation Analysis**: The pipeline computes the correlation between the two filtered channels across sliding windows.
*   **Smoothing**: A **Gaussian window** is applied to the resulting correlation trace to produce a smooth EMG envelope.

### 6. Final Alignment and Export
The final step involves precisely aligning all data streams—HPC, PFC, and the newly created EMG—to a uniform length.
*   **Trimming**: Signals are reshaped to a final common size of **1,342,539 samples**.
*   **Export**: The cleaned, downsampled, and synchronized data are saved as `HPC1.csv`, `PFC1.csv`, and `EMG1.csv` for use in machine learning models or further statistical analysis.

