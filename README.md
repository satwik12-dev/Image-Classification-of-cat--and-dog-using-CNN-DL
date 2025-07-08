
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
├── x_test.npy             # Test images (from Drive)
├── y_test.npy             # Test labels (from Drive)
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── .gitignore             # Git ignored files
```

---

## 📋 .gitignore Example

```
__pycache__/
*.pyc
*.ipynb_checkpoints/
*.npy
*.h5
*.keras
.env
.venv/
.DS_Store
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
📧 Email: satwik.yourmail@example.com  
🔗 GitHub: [satwik12-dev](https://github.com/satwik12-dev)  
🔗 LinkedIn: [Your LinkedIn URL](https://linkedin.com/in/your-link)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

Thanks to the open-source ML and Python community for tools like TensorFlow and Streamlit.
