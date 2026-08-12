# Retinal Eye Disease Detection System

A Streamlit portfolio application built around a two-stage EfficientNetB3 inference pipeline for retinal fundus images.

## Project structure

```text
.
├── app.py
├── recommendation.py
├── requirements.txt
├── MODEL1/
│   └── eye_disease_weights.npy
└── MODEL3/
    └── dr_subclassifier_weights.npy
```

The training datasets, notebooks, plots, SavedModel directory, `.h5` copies, cache files, and local machine paths are intentionally excluded from this deployment copy. The Streamlit application only needs the two NumPy weight files for inference.

## Run locally

Use Python 3.10, create a virtual environment, install `requirements.txt`, then run:

```bash
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

1. Push this folder to a GitHub repository.
2. In Streamlit Community Cloud, choose the repository, `main` branch, and `app.py` as the entrypoint.
3. In **Advanced settings**, select **Python 3.10**.
4. Deploy.

The app is intended as an educational/research portfolio demonstration and is not a medical diagnostic tool.
