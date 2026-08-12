from pathlib import Path
import tempfile

import cv2
import numpy as np
import streamlit as st
import tensorflow as tf

from tensorflow.keras import regularizers
from tensorflow.keras.layers import BatchNormalization, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adamax

from recommendation import (
    armd,
    cataract,
    glaucoma,
    mild,
    moderate,
    no_dr,
    normal,
    proliferate_dr,
    severe,
)

st.set_page_config(
    page_title="Eye Disease Detection Platform",
    page_icon="👁️",
    layout="centered",
)

# All paths are relative to the repository, so the app works locally and in the cloud.
BASE_DIR = Path(__file__).resolve().parent
MODEL1_WEIGHTS = BASE_DIR / "MODEL1" / "eye_disease_weights.npy"
MODEL2_WEIGHTS = BASE_DIR / "MODEL3" / "dr_subclassifier_weights.npy"

MODEL1_CLASSES = [
    "ARMD",
    "cataract",
    "diabetic_retinopathy",
    "glaucoma",
    "normal",
]
MODEL2_CLASSES = ["Mild", "Moderate", "No_DR", "Proliferate_DR", "Severe"]

_model1 = None
_model2 = None


def build_efficientnetb3(num_classes):
    base = tf.keras.applications.efficientnet.EfficientNetB3(
        include_top=False,
        weights=None,
        input_shape=(224, 224, 3),
        pooling="max",
    )
    model = Sequential(
        [
            base,
            BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001),
            Dense(
                256,
                kernel_regularizer=regularizers.l2(0.016),
                activity_regularizer=regularizers.l1(0.006),
                bias_regularizer=regularizers.l1(0.006),
                activation="relu",
            ),
            Dropout(rate=0.45, seed=123),
            Dense(num_classes, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=Adamax(learning_rate=0.001),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def get_model1():
    global _model1
    if _model1 is None:
        with st.spinner("Loading disease detection model..."):
            _model1 = build_efficientnetb3(len(MODEL1_CLASSES))
            weights = np.load(MODEL1_WEIGHTS, allow_pickle=True)
            _model1.set_weights(list(weights))
    return _model1


def get_model2():
    global _model2
    if _model2 is None:
        with st.spinner("Loading DR subclassifier model..."):
            _model2 = build_efficientnetb3(len(MODEL2_CLASSES))
            weights = np.load(MODEL2_WEIGHTS, allow_pickle=True)
            _model2.set_weights(list(weights))
    return _model2


def apply_gaussian_filter(img_array):
    img = img_array.astype(np.uint8)
    return cv2.addWeighted(
        img,
        4,
        cv2.GaussianBlur(img, (0, 0), 30),
        -4,
        128,
    )


def model_prediction(test_image_path):
    img = tf.keras.utils.load_img(test_image_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    x_batch = np.expand_dims(x, axis=0)

    # Stage 1: classify the eye image into one of five disease classes.
    pred1 = get_model1().predict(x_batch, verbose=0)
    class1 = MODEL1_CLASSES[int(np.argmax(pred1))]
    conf1 = float(np.max(pred1)) * 100

    # Stage 2: if DR is detected, classify its severity.
    if class1 == "diabetic_retinopathy":
        x_filt = apply_gaussian_filter(x)
        x_filt = np.expand_dims(x_filt, axis=0)
        pred2 = get_model2().predict(x_filt, verbose=0)

        no_dr_index = MODEL2_CLASSES.index("No_DR")
        pred2[0][no_dr_index] = 0
        class2 = MODEL2_CLASSES[int(np.argmax(pred2))]
        conf2 = float(np.max(pred2) / pred2.sum()) * 100
        return class1, class2, conf1, conf2

    return class1, None, conf1, None


st.sidebar.title("Dashboard")
st.sidebar.caption("Educational portfolio demonstration — not a medical diagnosis.")
app_mode = st.sidebar.selectbox(
    "Select Page", ["Home", "About", "Disease Identification"]
)

if app_mode == "Home":
    st.title("Eye Disease Detection Platform")
    st.markdown(
        """
        Welcome to the **Eye Disease Detection Analysis Platform**.

        This project demonstrates a two-stage deep-learning pipeline for retinal fundus-image classification.

        ### How It Works
        - **Stage 1:** EfficientNetB3 classifies an uploaded image as ARMD, Cataract,
          Diabetic Retinopathy, Glaucoma, or Normal.
        - **Stage 2:** When Stage 1 detects Diabetic Retinopathy, a second EfficientNetB3
          classifier estimates the DR severity.

        ### Disease Classes
        | Class | Description |
        |---|---|
        | **Normal** | No visible abnormality detected by the model |
        | **ARMD** | Age-related macular degeneration |
        | **Cataract** | Cataract classification |
        | **Glaucoma** | Glaucoma classification |
        | **Diabetic Retinopathy — Mild** | Mild DR stage |
        | **Diabetic Retinopathy — Moderate** | Moderate DR stage |
        | **Diabetic Retinopathy — Severe** | Severe DR stage |
        | **Diabetic Retinopathy — Proliferative** | Proliferative DR stage |

        Go to **Disease Identification** to test an image.
        """
    )

elif app_mode == "About":
    st.header("About the Project")
    st.markdown(
        """
        ### Model Architecture
        Both classifiers use **EfficientNetB3** with a custom classification head:
        - BatchNormalization
        - Dense(256) with L1/L2 regularization
        - Dropout(0.45)
        - Softmax output layer

        ### Model 1 — Eye Disease Detection
        - Five classes: ARMD, Cataract, Diabetic Retinopathy, Glaucoma, Normal
        - Reported project accuracy: **94.93%**

        ### Model 2 — Diabetic Retinopathy Subclassifier
        - Five classes: Mild, Moderate, Severe, Proliferative DR, No DR
        - Uses Gaussian preprocessing to enhance retinal-vessel contrast
        """
    )
    st.info(
        "This application is a student/research portfolio project. Predictions are not a substitute for examination or diagnosis by a qualified eye-care professional."
    )

elif app_mode == "Disease Identification":
    st.header("Eye Disease Analysis")
    test_image = st.file_uploader(
        "Upload an eye fundus image:", type=["jpg", "jpeg", "png"]
    )

    if test_image is not None:
        image_bytes = test_image.getvalue()
        st.image(image_bytes, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                tmp_file.write(image_bytes)
                temp_file_path = tmp_file.name

            try:
                with st.spinner("Analyzing image..."):
                    class1, class2, conf1, conf2 = model_prediction(temp_file_path)

                if class2 is not None:
                    st.success(
                        f"Stage 1 Result: **Diabetic Retinopathy** ({conf1:.1f}% confidence)"
                    )
                    st.success(
                        f"Stage 2 Result: **{class2}** ({conf2:.1f}% confidence)"
                    )
                    final_label = f"Diabetic Retinopathy — {class2}"
                else:
                    st.success(f"Result: **{class1}** ({conf1:.1f}% confidence)")
                    final_label = class1

                st.markdown(f"### Model Output: {final_label}")
                st.markdown("---")

                with st.expander("Learn More & Recommendations"):
                    if class1 == "normal":
                        st.markdown(normal)
                    elif class1 == "cataract":
                        st.markdown(cataract)
                    elif class1 == "glaucoma":
                        st.markdown(glaucoma)
                    elif class1 == "ARMD":
                        st.markdown(armd)
                    elif class1 == "diabetic_retinopathy":
                        recommendations = {
                            "Mild": mild,
                            "Moderate": moderate,
                            "Severe": severe,
                            "Proliferate_DR": proliferate_dr,
                            "No_DR": no_dr,
                        }
                        st.markdown(recommendations[class2])

                    st.caption(
                        "The recommendation text is informational only and does not constitute medical advice."
                    )
            finally:
                Path(temp_file_path).unlink(missing_ok=True)
