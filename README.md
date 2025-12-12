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
├── 00_data/                     # Stockage des datasets (bruts et processés)
│
├── 01_preprocessing/            # Scripts de nettoyage et transformation des données
│
├── 02_cnn_approach/             # Expérimentations avec l'architecture CNN
│   ├── 2.0_cnn_model/           # Entraînement du modèle CNN supervisé
│   ├── 2.1_unsupervised/        # Approche non-supervisée sur l'ensemble des données
│   └── 2.2_unsupervised_by_state/ # Approche non-supervisée segmentée par état
│
├── 03_full_unsupervised/        # Modélisation entièrement non-supervisée (clustering, etc.)
│
├── 04_deploy_hf/                # Fichiers pour le déploiement (ex: Hugging Face Spaces)
│
└── 05_visualization/            # Génération des graphiques et analyse des résultats

```

## Useful Links

- [Review on automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/36479908/)
- [Pros and cons of automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/37889222/)
- [Infographic summary from ESRS](https://esrs.eu/wp-content/uploads/2024/02/INFOGRAPHIC-Rodent-sleep-scoring.pdf)
- [Recent article on biological data tools](https://www.nature.com/articles/s42003-025-07991-3)


