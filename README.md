# 🐾 Cats vs Dogs Image Classifier

This project is a simple and interactive web application built using **Streamlit** that classifies uploaded images as either **Cat** or **Dog** using a pre-trained deep learning model.

## 📌 Project Overview

- **Goal**: Predict whether an uploaded image is a cat or a dog.
- **Model Used**: A Convolutional Neural Network (CNN) trained on a labeled dataset of cat and dog images.
- **Frontend**: Built using Streamlit for a clean and user-friendly interface.
- **Backend**: Utilizes TensorFlow/Keras for model loading and image classification.

## 🚀 Features

- Upload image from local system or provide an online image URL.
- Real-time prediction with confidence score.
- Clean, responsive UI with custom CSS styling.
- Graphical confidence score (optional to extend).
- Caching enabled for model loading to improve performance.

## 📂 File Structure

- `app2.py`: Main Streamlit app file to run the web application.
- `cats_vs_dogs.keras`: Trained CNN model saved in Keras format.
- `README.md`: Project documentation and instructions.
- `requirements.txt`: Python packages required to run the app.

## 🖼️ How It Works

1. User uploads an image or pastes an image URL.
2. Image is resized to 150x150 pixels and normalized.
3. The model predicts if it's a cat or a dog.
4. The result and confidence score are displayed.

## 📥 Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/cats-vs-dogs-classifier.git
    cd cats-vs-dogs-classifier
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app2.py
    ```

## 🧪 Requirements

- Python 3.7+
- Streamlit
- TensorFlow
- Pillow
- NumPy
- Plotly

> Install them using: `pip install streamlit tensorflow pillow numpy plotly`

## 🧠 Model Details

- Input Size: 150x150 RGB images
- Architecture: CNN with Conv2D, MaxPooling, BatchNormalization, Dense layers
- Output: Binary classification (`0 = Cat`, `1 = Dog`)
- Training Dataset: Based on Kaggle Dogs vs. Cats Dataset

## ✨ Example

![App Screenshot]()

## 🙌 Acknowledgments

- [Kaggle Dogs vs. Cats Dataset](https://www.kaggle.com/c/dogs-vs-cats/data)
- [Keras Documentation](https://keras.io/)
- [Streamlit Docs](https://docs.streamlit.io/)

---

👨‍💻 **Made with ❤️ by Satwik Saxena**

# 🐶🐱 Dog vs Cat Image Classification using CNN + Streamlit

An AI-powered web application that classifies images as either a **dog** or a **cat** using a trained deep learning model (CNN). The project uses **TensorFlow**, **Keras**, and **Streamlit** for building and serving the model, providing real-time predictions with confidence levels.

---

## 📸 Live Demo

> 🟡 Currently not deployed online. You can run it locally by following the instructions below.

---

## 📂 Download Required Files

Due to file size limits on GitHub, you can download the necessary files from Google Drive:

- 📂 [Download DataSets (input.csv, labels.csv, input_test.csv, labels_test.csv,x_test.npy, y_test.npy)](https://drive.google.com/drive/folders/1GKyDuHlT7LzthTGyxbqjuZSCZWaBzkkh?usp=sharing )

> Place these files directly in the root project folder after downloading.

---

## 🚀 Features

- Upload an image (`.jpg`, `.jpeg`, `.png`, `.webp`)
- Real-time classification: Cat 🐱 or Dog 🐶
- Displays:
  - Predicted class
  - Confidence percentage
  - Model test accuracy
- Clean web UI using **Streamlit**
- Automatically resizes, normalizes, and reshapes input images for the model

---

## 🧠 Model Information

- **Model Type:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow / Keras
- **Input Size:** 100 x 100 RGB images
- **Output:** Binary classification using sigmoid activation
  - ≥ 60% → Cat 🐱
  - ≤ 40% → Dog 🐶
  - Between → Not Identified ❓
- **Test Accuracy:** ~90%

---

## 🧪 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/satwik12-dev/Image-Classification-of-cat--and-dog-using-CNN-DL.git
cd Image-Classification-of-cat--and-dog-using-CNN-DL
```

### 2️⃣ Set Up Environment & Install Dependencies

(Optional but recommended: create virtual environment)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Then install packages:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, use:

```bash
pip install streamlit tensorflow numpy pillow
```

### 3️⃣ Download & Add Model + Test Files

Manually download from the Google Drive links above and place them in the project root:
- `x_test.npy`
- `y_test.npy`

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Then open the link in your browser (usually http://localhost:8501).

---

## 🗂️ Project Structure

```
Image-Classification-of-cat--and-dog-using-CNN-DL/
├── app.py                 # Streamlit web app
├── IC.keras               # Pre-trained CNN model (from Drive)
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── .gitignore             # Git ignored files
```

---

## 🔧 To Do / Future Improvements

- Deploy the app online (Streamlit Cloud or Hugging Face)
- Improve confidence thresholds
- Add drag & drop image upload
- Extend to more animal categories (multi-class)
- Add animated feedback or visualizations

---

## 🧑‍💻 Author

**Satwik Saxena**  
📧 Email: satwiksaxena41@gmail.com  
🔗 GitHub: [satwik12-dev](https://github.com/satwik12-dev)  
🔗 LinkedIn: [satwik-12-dev](https://linkedin.com/in/satwik-12-dev)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

Thanks to the open-source ML and Python community for tools like TensorFlow and Streamlit.
