<div align="center">

<img src="learnn.jpg" alt="NeuroSense Banner" width="100%"/>

<br/>

# 🧠 NeuroSense

### *See the Signs. Support the Mind.*

> A deep learning–powered web application that detects early signs of **Dyslexia** by analyzing handwriting samples in real-time using Convolutional Neural Networks.

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-CNN%20Model-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Styled-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

[🚀 Getting Started](#-getting-started) · [🧪 How It Works](#-how-it-works) · [📁 Project Structure](#-project-structure) · [🤝 Contributing](#-contributing)

</div>

---

## 🌟 What is NeuroSense?

**NeuroSense** is an AI-powered assistive tool that helps identify early indicators of **Dyslexia** — a learning difference affecting how the brain processes written language — through the analysis of handwriting samples.

By leveraging a custom **Convolutional Neural Network (CNN)**, NeuroSense processes uploaded handwriting images and provides a real-time prediction, enabling educators, parents, and clinicians to take timely, informed action.

> 💡 **Did you know?** Dyslexia affects approximately **15–20% of the population**, yet early detection significantly improves outcomes. NeuroSense bridges the gap between cutting-edge AI and accessible screening tools.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖼️ **Handwriting Upload** | Upload any handwriting image for instant analysis |
| 🤖 **CNN-Based Detection** | Deep learning model trained on real dyslexia datasets |
| ⚡ **Real-Time Results** | Instant prediction with confidence output |
| 🌐 **Web Interface** | Clean, accessible browser-based UI — no installation needed for users |
| 📊 **Jupyter Notebook** | Fully documented model training workflow |
| 🗂️ **Organized Datasets** | Structured dataset folders for reproducible training |

---

## 🧪 How It Works

```
📸 Upload Handwriting Image
        ↓
🔍 Image Preprocessing (resize, normalize)
        ↓
🧠 CNN Model Inference
        ↓
📊 Prediction: Dyslexic / Non-Dyslexic
        ↓
🌐 Result Displayed on Web Interface
```

The model is trained on labeled handwriting samples, learning to identify spatial patterns, letter reversals, inconsistent spacing, and other visual signatures commonly associated with dyslexia.

---

## 📁 Project Structure

```
NeuroSense/
│
├── 📂 dataset/               # Raw dataset for training
├── 📂 dyslexia_dataset/      # Processed dyslexia-specific samples
├── 📂 static/                # CSS, JS, images for the web app
├── 📂 templates/             # HTML templates (Jinja2 / Flask)
│
├── 🐍 app.py                 # Flask web application entry point
├── 🐍 train_model.py         # CNN model training script
├── 📓 NeuroSense.ipynb       # Jupyter notebook — EDA & model training
├── 📋 requirements.txt       # Python dependencies
├── 🖼️ learnn.jpg             # Project visual / banner
└── 📄 README.md              # You're reading it!
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Rithika48/NeuroSense.git
cd NeuroSense
```

**2. Create a virtual environment** *(recommended)*
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Train the model** *(skip if pre-trained model is included)*
```bash
python train_model.py
```

**5. Launch the web app**
```bash
python app.py
```

**6. Open your browser and go to:**
```
http://127.0.0.1:5000
```

---

## 🧠 Model Architecture

The CNN model is built to classify handwriting samples into:

- ✅ **Non-Dyslexic** — Handwriting patterns within typical range
- ⚠️ **Dyslexic Indicators** — Patterns suggesting early signs of dyslexia

The model uses standard CNN layers (Conv2D → MaxPooling → Dropout → Dense) optimized for grayscale handwriting image classification. Full architecture details are available in [`NeuroSense.ipynb`](NeuroSense.ipynb).

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Deep Learning** | TensorFlow / Keras |
| **Frontend** | HTML5, CSS3 |
| **Model Development** | Jupyter Notebook |
| **Data Handling** | NumPy, OpenCV / Pillow |

---

## 📸 Screenshots

> *Upload your handwriting image → Get an instant AI-powered assessment*

| Home Page | Upload & Predict | Result View |
|---|---|---|
| *(Screenshot)* | *(Screenshot)* | *(Screenshot)* |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help improve NeuroSense:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

---

## ⚠️ Disclaimer

> NeuroSense is an **educational and screening aid** — it is **not a medical diagnostic tool**. Results should not replace professional evaluation by a licensed educational psychologist, neurologist, or learning specialist. Always consult a qualified professional for a formal assessment.

---

## 👩‍💻 Author

<div align="center">

**Rithika**

[![GitHub](https://img.shields.io/badge/GitHub-Rithika48-181717?style=for-the-badge&logo=github)](https://github.com/Rithika48)

*"Building technology that understands how people learn differently."*

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ and a belief that **every mind deserves to be understood**

⭐ Star this repo if NeuroSense inspired you!

</div>
