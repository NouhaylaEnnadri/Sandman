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

## Useful Links

- [Review on automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/36479908/)
- [Pros and cons of automatic sleep scoring](https://pubmed.ncbi.nlm.nih.gov/37889222/)
- [Infographic summary from ESRS](https://esrs.eu/wp-content/uploads/2024/02/INFOGRAPHIC-Rodent-sleep-scoring.pdf)
- [Recent article on biological data tools](https://www.nature.com/articles/s42003-025-07991-3)


