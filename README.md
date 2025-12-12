# Sandman

**Sleep Architecture: Building Smarter Tools for Biological Data**

## Dataset Structure

- **Rats**: Each rat has its own folder (e.g., `1/`, `3/`, `4/`).
- **Experiments**: 5 per rat, each with:
  - **HPC_XXX** – hippocampal recordings (2500 Hz).
  - **PFC_XXX** – prefrontal cortex recordings (2500 Hz).
  - **Post_trialX_XXX-states.mat** – manually annotated sleep/behavioral states (1 Hz).
- **Pre-sleep folders**: Present but not used.
- **Focus**: We only use the `states` variable from post-trials, paired with raw neural signals.

## Project Structure

The project is organized into two main distinct approaches: a CNN-based approach (semi-supervised/hybrid) and a Fully Unsupervised approach.


```bash
├── 00_data/                     # Stockage of datasets (raw and preprocessed)
│
├── 01_preprocessing/            # Preprocessing and analyse through K-means
│
├── 02_cnn_approach/             # Experimentation on CNN
│   ├── 2.0_cnn_model/           # CNN model
│   ├── 2.1_unsupervised/        # Unsupervised approach on the full data already labelled with the CNN
│   └── 2.2_unsupervised_by_state/ # Unsupervised approach on the data divided by state
│
├── 03_full_unsupervised/        # Modelisation fully unsupervised (clustering, etc.)
│
├── 04_deploy_hf/                # Files for the deployement on Hugging Face Spaces
│
└── 05_visualization/            # Script for the vizualisation (2D and 3D) 

```

## Useful Links

- [Review on automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/36479908/)
- [Pros and cons of automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/37889222/)
- [Infographic summary from ESRS](https://esrs.eu/wp-content/uploads/2024/02/INFOGRAPHIC-Rodent-sleep-scoring.pdf)
- [Recent article on biological data tools](https://www.nature.com/articles/s42003-025-07991-3)


