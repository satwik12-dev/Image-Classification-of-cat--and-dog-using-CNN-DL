import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import plotly.graph_objects as go

# Configure Streamlit
st.set_page_config(page_title="🐱🐶 Cats vs Dogs Classifier", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        html, body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f7f7f7;
        }
        .main {
            padding: 2rem;
        }
        .stButton>button {
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #e8e8e8;
            text-align: center;
            padding: 12px;
            font-size: 14px;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🐾 Cats vs Dogs Classifier")
st.markdown("Upload an image of a **cat or dog**, and the model will predict the class with confidence!")

# Load the trained model
@st.cache_resource
def load_trained_model():
    return load_model("cats_vs_dogs.keras")

model = load_trained_model()
class_labels = {0: "Cat", 1: "Dog"}

# Image preprocessing
def preprocess_image(img: Image.Image) -> np.ndarray:
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

upload_method = st.radio("Choose image upload method:", ["Upload from local system", "Enter image URL"])

img = None

# Option 1: Upload from local system
if upload_method == "Upload from local system":
    uploaded_img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_img:
        img = Image.open(uploaded_img)

# Option 2: Upload via URL
else:
    img_url = st.text_input("🔗 Enter the image URL")
    if img_url:
        try:
            from urllib.request import urlopen
            img = Image.open(urlopen(img_url))
        except Exception as e:
            st.error("Failed to load image. Please check the URL.")

# If image is provided, process and predict
if img:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(img, caption="Input Image", use_container_width=True)

    with col2:
        with st.spinner("🔍 Predicting..."):
            img_batch = preprocess_image(img)
            pred = model.predict(img_batch)[0][0]
            pred_class = int(pred > 0.5)
            confidence = pred if pred_class == 1 else 1 - pred
            prob_dog = float(pred)
            prob_cat = float(1 - pred)

        st.markdown(f"### **Prediction:** `{class_labels[pred_class]}`")
        st.markdown(f"### **Confidence:** `{confidence:.2%}`")

        
# Footer
st.markdown("""
    <div class="footer">
        Made with by <b>Satwik Saxena</b>
    </div>
""", unsafe_allow_html=True)

# Hide Streamlit's default footer
st.markdown("""
    <style>
        footer {visibility: hidden;}
        .stApp {
            bottom: 0;
            position: fixed;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)