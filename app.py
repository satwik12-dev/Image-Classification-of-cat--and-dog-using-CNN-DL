import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model('IC.keras')

# Load test data for accuracy display
x_test = np.load('x_test.npy')
y_test = np.load('y_test.npy')

loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

# Streamlit app title
st.title("🐶 Dog vs 🐱 Cat Image Classifier")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Load and display image
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Preprocess image
    img = image.resize((100, 100))
    img_arr = np.array(img) / 255.0
    img_arr = img_arr.reshape(1, 100, 100, 3)

    # Predict
    prediction = model.predict(img_arr)[0][0]  # Assuming sigmoid output

    # Set thresholds
    confidence_threshold = 0.6  # You can adjust this value

    if prediction >= confidence_threshold:
        pred = 'Cat 🐱'
        confidence_percent = prediction * 100
    elif prediction <= (1 - confidence_threshold):
        pred = 'Dog 🐶'
        confidence_percent = (1 - prediction) * 100
    else:
        pred = 'Not Identified ❓'
        confidence_percent = max(prediction, 1 - prediction) * 100

    # Display results
    st.markdown(f"### Prediction: **{pred}**")
    st.markdown(f"### Confidence: **{confidence_percent:.2f}%**")
    st.markdown(f"### Model Accuracy on Test Set: **{accuracy * 100:.2f}%**")

