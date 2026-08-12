# 👁️ Retinal Eye Disease Detection System

A Streamlit-based deep-learning application for classifying retinal fundus images using a **two-stage EfficientNetB3 inference pipeline**.

🔗 **Live Demo:** https://yash-eye-disease-detection.streamlit.app/

> ⚠️ **Disclaimer:** This project is an educational/research portfolio demonstration. It is not a medical diagnostic tool. Model predictions should not be used as a substitute for evaluation by a qualified eye-care professional.

---

## 📌 Overview

This project demonstrates a deep-learning image-classification pipeline for retinal fundus images.

The application uses **two EfficientNetB3 models**:

* **Stage 1 — Eye Disease Classifier**

  * Classifies a retinal fundus image into one of five categories:

    * ARMD
    * Cataract
    * Diabetic Retinopathy
    * Glaucoma
    * Normal

* **Stage 2 — Diabetic Retinopathy Subclassifier**

  * Activated when Stage 1 identifies Diabetic Retinopathy.
  * Estimates the diabetic retinopathy severity:

    * Mild
    * Moderate
    * Severe
    * Proliferative DR
    * No DR

The application also provides informational recommendations associated with the predicted category.

---

## 🧠 Model Pipeline

```text
                    Retinal Fundus Image
                             │
                             ▼
                  ┌─────────────────────┐
                  │     EfficientNetB3  │
                  │       Stage 1       │
                  └──────────┬──────────┘
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
        ARMD             Cataract            Glaucoma
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                           Normal
                             │
                             │
                  Diabetic Retinopathy
                             │
                             ▼
                  Gaussian Preprocessing
                             │
                             ▼
                  ┌─────────────────────┐
                  │     EfficientNetB3  │
                  │       Stage 2       │
                  └──────────┬──────────┘
                             │
                             ▼
                       DR Severity
```

---

## 🔬 Model Architecture

Both classifiers use **EfficientNetB3** with a custom classification head consisting of:

* BatchNormalization
* Dense(256)
* L1/L2 regularization
* Dropout(0.45)
* Softmax output layer

### Model 1 — Eye Disease Detection

Five-class classifier:

| Class                    | Description                                  |
| ------------------------ | -------------------------------------------- |
| **ARMD**                 | Age-related macular degeneration             |
| **Cataract**             | Cataract classification                      |
| **Diabetic Retinopathy** | Detection of diabetic retinopathy            |
| **Glaucoma**             | Glaucoma classification                      |
| **Normal**               | No visible abnormality detected by the model |

**Reported project accuracy:** 94.93%

### Model 2 — Diabetic Retinopathy Subclassifier

Five-class classifier:

| Class                | Description                        |
| -------------------- | ---------------------------------- |
| **Mild**             | Mild diabetic retinopathy          |
| **Moderate**         | Moderate diabetic retinopathy      |
| **Severe**           | Severe diabetic retinopathy        |
| **Proliferative DR** | Proliferative diabetic retinopathy |
| **No DR**            | No diabetic retinopathy            |

The Stage 2 classifier uses **Gaussian preprocessing** to enhance retinal-vessel contrast before inference.

---

## 🚀 Features

* 🖼️ Upload retinal fundus images in JPG, JPEG, or PNG format
* 🧠 Two-stage EfficientNetB3 inference pipeline
* 🔍 Five-class primary eye-disease classification
* 🩺 Diabetic retinopathy severity classification
* 📊 Confidence scores for model predictions
* 📚 Informational recommendations for detected categories
* 🖥️ Streamlit web interface
* ☁️ Deployed using Streamlit Community Cloud

---

## 📂 Project Structure

```text
eye-disease-detection/
│
├── app.py
├── recommendation.py
├── requirements.txt
├── README.md
│
├── MODEL1/
│   └── eye_disease_weights.npy
│
└── MODEL3/
    └── dr_subclassifier_weights.npy
```

The deployment repository intentionally excludes the original training datasets, notebooks, plots, SavedModel directories, `.h5` copies, cache files, and local machine paths.

The deployed application only requires the two NumPy weight files for inference.

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* EfficientNetB3
* OpenCV
* NumPy
* Streamlit
* Pillow

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Yash-2099/eye-disease-detection.git
cd eye-disease-detection
```

### 2. Use Python 3.10

This project uses **TensorFlow 2.10.0**, which requires a compatible Python environment.

Create a virtual environment:

```bash
python3.10 -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment configuration:

* **Repository:** `Yash-2099/eye-disease-detection`
* **Branch:** `main`
* **Main file:** `app.py`
* **Python:** 3.10

### Live Application

🔗 **https://yash-eye-disease-detection.streamlit.app/**

---

## 📊 Application Workflow

1. Open the application.
2. Navigate to **Disease Identification**.
3. Upload a retinal fundus image.
4. Click **Predict**.
5. The Stage 1 EfficientNetB3 model analyzes the image.
6. If Diabetic Retinopathy is detected, the image is processed using Gaussian filtering.
7. The Stage 2 model estimates the DR severity.
8. The application displays the predicted class and confidence.
9. Informational recommendations are displayed based on the result.

---

## 📚 Recommendations

The application includes informational content for the detected categories, including:

* Normal
* ARMD
* Cataract
* Glaucoma
* Mild diabetic retinopathy
* Moderate diabetic retinopathy
* Severe diabetic retinopathy
* Proliferative diabetic retinopathy
* No diabetic retinopathy

These recommendations are intended for **educational purposes only**.

---

## ⚠️ Disclaimer

This application is intended for **educational and research portfolio purposes only**.

The model predictions are **not medical diagnoses**. Retinal images and predictions should be evaluated by a qualified eye-care professional before any medical decision is made.

Do not use this application to diagnose, treat, or rule out an eye condition.

If you experience significant or sudden changes in vision, seek appropriate professional medical evaluation.

---

## 👨‍💻 Project

Built as a deep-learning and computer-vision portfolio project demonstrating:

* Image classification
* Transfer-learning architecture
* Multi-stage inference
* Retinal image preprocessing
* TensorFlow/Keras model deployment
* Streamlit application development
* Cloud deployment

---
