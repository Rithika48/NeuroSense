# <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=35&pause=1000&color=6C63FF&width=600&lines=🧠+NeuroSense;Early+Dyslexia+Detection+AI" alt="NeuroSense" />

<div align="center">

![NeuroSense Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=NeuroSense&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Early%20Dyslexia%20Detection%20from%20Handwriting%20using%20CNN&descAlignY=55&descSize=18)

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![CNN](https://img.shields.io/badge/Model-CNN-E34F26?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> 🏆 **Built during AETHERION'25** — 24-Hour Hackathon at Canara Engineering College

<br/>

**NeuroSense** is an AI-powered web application that detects early signs of **Dyslexia** from handwriting samples in real-time using a Convolutional Neural Network (CNN) — making early screening faster, accessible, and affordable for everyone.

<br/>

[🚀 View Demo](#-demo) • [⚙️ Installation](#-how-to-run-locally) • [🧠 Model](#-model-architecture) • [🤝 Contribute](#-contributing)

</div>

---

## 🌟 Why NeuroSense?

<div align="center">

| 🌍 Problem | 💡 Solution |
|---|---|
| 1 in 10 people worldwide have Dyslexia | AI-powered early detection |
| Clinical diagnosis is expensive | Free, accessible web tool |
| Lack of awareness in schools | Real-time handwriting analysis |
| Delayed detection affects learning | Instant prediction with confidence score |

</div>

---

## ✨ Features

```
🔍  Upload any handwriting image for instant analysis
🤖  CNN model trained on real dyslexia handwriting dataset  
⚡  Real-time prediction with confidence score
🎯  Binary classification — Dyslexic / Non-Dyslexic
✅  Smart file validation — PNG/JPG/JPEG only
🌐  Clean, responsive web interface
📊  Confidence percentage displayed with every result
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| 🧠 **ML Model** | Convolutional Neural Network (CNN) |
| 🔥 **Deep Learning** | TensorFlow / Keras |
| 🐍 **Backend** | Python, Flask |
| 🎨 **Frontend** | HTML5, CSS3, JavaScript |
| 📊 **Data Processing** | NumPy, Pandas, OpenCV |
| 🔧 **Development** | Jupyter Notebook, VS Code |
| 📦 **Dependencies** | requirements.txt |

</div>

---

## 📁 Project Structure

```
🧠 NeuroSense/
│
├── 📄 app.py                   # Flask web application & routes
├── 🤖 train_model.py           # CNN model training script
├── 📓 NeuroSense.ipynb         # Model exploration notebook
│
├── 📂 dataset/                 # Training dataset
├── 📂 dyslexia_dataset/        # Dyslexia specific samples
├── 📂 sample_images/           # Sample test images
│
├── 📂 static/                  # CSS, JS, images
│   ├── style.css
│   └── script.js
│
├── 📂 templates/               # HTML templates
│   ├── index.html              # Upload page
│   └── result.html             # Prediction result page
│
├── 📄 requirements.txt         # Python dependencies
├── 📄 .gitignore
└── 📄 README.md
```

---

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.8+
- pip package manager
- Webcam (optional)

### Steps

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Rithika48/NeuroSense.git

# 2️⃣ Navigate to project folder
cd NeuroSense

# 3️⃣ Create virtual environment
python -m venv venv

# 4️⃣ Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 5️⃣ Install dependencies
pip install -r requirements.txt

# 6️⃣ Run the application
python app.py

# 7️⃣ Open in browser
# Visit: http://localhost:5000
```

---

## 🧠 Model Architecture

```
📸 Input Image (Handwriting Sample)
           │
           ▼
    ┌─────────────────┐
    │  Conv2D Layer   │  ← Feature extraction
    │  + ReLU         │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  MaxPooling     │  ← Dimensionality reduction
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  Conv2D Layer   │  ← Deep feature learning
    │  + ReLU         │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  MaxPooling     │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  Flatten Layer  │
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │  Dense Layer    │  ← Classification
    └────────┬────────┘
             │
             ▼
    🎯 Output: Dyslexic / Non-Dyslexic
    📊 + Confidence Score %
```

---

## 🔄 How It Works

```
Step 1 → User uploads handwriting image 📸
Step 2 → Image preprocessed (resize + normalize) ⚙️
Step 3 → CNN model analyzes handwriting patterns 🧠
Step 4 → Prediction generated with confidence % 📊
Step 5 → Result displayed on web interface ✅
```

---

## 🧪 Test the App

Sample handwriting images are available in the `/sample_images/` folder!

You can use these to **test the application** without needing your own dataset.

---

## 🚀 Future Improvements

- [ ] 🔍 Add **Grad-CAM visualization** to highlight dyslexic patterns
- [ ] 📱 Make UI **fully mobile responsive**
- [ ] 🔗 Build **REST API** for third-party integration
- [ ] 🌍 Add **multi-language** handwriting support
- [ ] 🏫 Integrate with **school management systems**
- [ ] 📈 Improve model accuracy with **larger dataset**
- [ ] ☁️ Deploy on **cloud platform** (AWS/Heroku)

---

## 🏆 Hackathon Achievement

<div align="center">

```
🎯 Event    : AETHERION'25
⏰ Duration : 24 Hours
🏫 Venue    : Canara Engineering College
📅 Date     : March 27-29, 2025
🚀 Built    : End-to-end CNN Web Application
```

> Built complete AI-powered web application from scratch in **24 hours** — from problem ideation to working deployed solution!

</div>

---

## 📦 Requirements

```txt
flask
tensorflow
keras
numpy
pillow
scikit-learn
matplotlib
opencv-python
```

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are always welcome! 🎉

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/AmazingFeature

# 3. Commit your changes
git commit -m "Add AmazingFeature"

# 4. Push to branch
git push origin feature/AmazingFeature

# 5. Open a Pull Request
```

---

## 👩‍💻 About the Developer

<div align="center">

**Rithika Saroli**
*Final Year CS Student | AI/ML & Full Stack Developer*
*Mangaluru, Karnataka, India*

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rithika-saroli)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Rithika48)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rithikasaroli@gmail.com)

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer)

### ⭐ If you found NeuroSense helpful, please give it a star!
### It helps others discover this project and motivates further development! 🚀

**Made with ❤️ by Rithika Saroli**

</div>
