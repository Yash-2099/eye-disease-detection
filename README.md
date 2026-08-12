# Retinal Eye Disease Detection System

A Streamlit portfolio application for retinal fundus-image classification using a two-stage EfficientNetB3 inference pipeline.

## Live Demo

**Streamlit App:**  
https://yash-eye-disease-detection.streamlit.app/

> **Medical Disclaimer:** This application is an educational/research portfolio project. Its predictions are not a medical diagnosis and should not be used as a substitute for evaluation by a qualified eye-care professional.

## Overview

The application uses a two-stage deep-learning pipeline:

1. **Stage 1 — Eye Disease Classification**
   - EfficientNetB3-based classifier
   - Classifies an uploaded image into:
     - ARMD
     - Cataract
     - Diabetic Retinopathy
     - Glaucoma
     - Normal

2. **Stage 2 — Diabetic Retinopathy Subclassification**
   - Activated when Stage 1 predicts Diabetic Retinopathy
   - Uses a second EfficientNetB3-based classifier
   - Predicts:
     - Mild
     - Moderate
     - Severe
     - Proliferative DR
     - No DR

For Diabetic Retinopathy classification, Gaussian filtering is applied as part of the preprocessing pipeline before the second-stage prediction.

## Model Architecture

Both classifiers use an EfficientNetB3 backbone with a custom classification head consisting of:

- Batch Normalization
- Dense layer with 256 units
- L1/L2 regularization
- Dropout
- Softmax output layer

The trained models are deployed using NumPy weight files rather than the original training artifacts.

## Project Structure

```text
.
├── app.py
├── recommendation.py
├── requirements.txt
├── MODEL1/
│   └── eye_disease_weights.npy
└── MODEL3/
    └── dr_subclassifier_weights.npy
