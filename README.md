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
project_root/
│
├── 01_cnn_approach/
│   ├── 1a_cnn_supervised_model.ipynb        
│   ├── 1b_unsupervised_by_state.ipynb       
│   └── 1c_unsupervised_global_labeled.ipynb 
│
├── 02_full_unsupervised/
│   └── 2a_fully_unsupervised_model.ipynb
│
└── README.md
```
## Useful Links

- [Review on automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/36479908/)
- [Pros and cons of automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/37889222/)
- [Infographic summary from ESRS](https://esrs.eu/wp-content/uploads/2024/02/INFOGRAPHIC-Rodent-sleep-scoring.pdf)
- [Recent article on biological data tools](https://www.nature.com/articles/s42003-025-07991-3)


