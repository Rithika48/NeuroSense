# NeuroSense – AI-Based Dyslexia Detection from Handwriting

An AI-powered handwriting analysis system that detects early signs of Dyslexia using deep learning techniques. The platform analyzes handwriting images and predicts whether the writing pattern indicates Dyslexia or Non-Dyslexia.

The system uses **Computer Vision, Convolutional Neural Networks (CNN), and a Flask web application** to provide quick screening support for learning disabilities based on handwriting patterns.

---

# Project Description

This project is a web-based deep learning platform that detects potential Dyslexia in handwriting samples.

The application allows users to upload a handwriting image, which is then analyzed using a trained **Convolutional Neural Network (CNN)** model to identify writing patterns commonly associated with Dyslexia.

The system performs image preprocessing, feeds the processed image into the trained model, and returns a prediction indicating whether the handwriting sample shows characteristics of Dyslexia.

The platform aims to support early screening and assist educators, parents, and researchers in identifying learning difficulties at an early stage.

---

# Problem Statement

Learning disabilities such as Dyslexia often remain undiagnosed during early childhood due to limited access to specialized assessment tools.

Traditional diagnosis methods typically require:

- Professional psychological evaluation
- Time-consuming handwriting analysis
- Specialized educational assessments

Many schools and families lack access to early diagnostic tools that can help identify learning challenges quickly.

This project aims to address this problem by developing a **machine learning-based handwriting analysis system** that can provide early indications of Dyslexia using AI-based image analysis.

---

# Tech Stack

## Programming Languages
- Python
- HTML
- CSS
- JavaScript

## Backend
- Flask

## Deep Learning
- TensorFlow
- Keras

## Data Processing
- NumPy

## Image Processing
- TensorFlow Image Processing
- ImageDataGenerator

## Visualization / Interface
- HTML Templates
- Static CSS

## Data Storage
- Image Dataset

---

# Dataset

The model is trained using a dataset of handwriting samples from individuals with and without Dyslexia.

The dataset contains handwriting images categorized into two classes:

- Dyslexic handwriting
- Non-Dyslexic handwriting

These images allow the CNN model to learn patterns related to:

- letter spacing
- writing alignment
- stroke patterns
- irregular letter formation

---

# Example Dataset Format

```
dyslexia_dataset/
│
├── dyslexic/
│   ├── 1.jpeg        ← incorrectly named "image1", actually belongs here
│   ├── 2.jpeg
│   └── ...
│
└── non_dyslexic/
    ├── 1.jpeg
    ├── 2.jpeg
    └── ...
```

Each folder represents a classification category used during CNN model training.

---

# How to Run

## 1. Clone the Repository

```
git clone https://github.com/Rithika48/NeuroSense.git
```

## 2. Navigate to the Project Folder

```
cd NeuroSense
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

## 4. Run the Application

```
python app.py
```

## 5. Open in Browser

```
http://127.0.0.1:5000
```

Upload a handwriting image to receive the prediction result.

---

# System Architecture

```
User Uploads Handwriting Image
        │
        ▼
Web Interface (HTML/CSS)
        │
        ▼
Flask Web Application
        │
        ▼
Image Preprocessing
        │
        ▼
CNN Deep Learning Model
        │
        ▼
Dyslexia / Non-Dyslexia Prediction
```

The system processes uploaded images, prepares them for model input, and then feeds them into the trained CNN model to generate predictions.

---

# Project Structure

```
NeuroSense
│
├── dyslexia_dataset
│   ├── dyslexic
│   ├── non_dyslexic
│
├── models
│   └── dyslexia_model_best.h5
│
├── static
│   └── uploads
│
├── templates
│   └── index.html
│
├── NeuroSense.ipynb
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Deep Learning Model

The handwriting classification model is built using a **Convolutional Neural Network (CNN)**.

CNN models are highly effective for image-based pattern recognition tasks such as handwriting analysis.

---

# Features Used by the Model

The CNN automatically learns visual features from handwriting images including:

- Stroke curvature
- Letter spacing
- Alignment
- Character irregularities
- Writing patterns

---

# Model Workflow

1️⃣ Data Collection  
2️⃣ Image Preprocessing  
3️⃣ Data Augmentation  
4️⃣ CNN Model Training  
5️⃣ Model Evaluation  
6️⃣ Model Deployment using Flask

The trained model is saved as:

```
dyslexia_model_best.h5
```

and loaded during application startup for prediction.

---

# Screenshots

## Home Page

The home page allows users to upload handwriting images for analysis.

The interface provides a simple upload option and displays prediction results instantly.

<p align="center">
  <img src="Home1(2).png" width="45%" />
  <img src="Home2(2).png" width="45%" />
</p>

---

## Prediction Result Page

After uploading an image, the system processes the handwriting and displays whether the sample indicates **Dyslexia or Non-Dyslexia**.

---

# Future Improvements

Possible future enhancements include:

- Using larger handwriting datasets
- Improving model accuracy with advanced CNN architectures
- Implementing handwriting segmentation techniques
- Deploying the application on cloud platforms
- Building a mobile application version
- Adding Explainable AI visualization for predictions

---

# Impact

This project demonstrates how **Artificial Intelligence, Computer Vision, and Deep Learning** can be used to assist in the early detection of learning disabilities.

By analyzing handwriting patterns through AI, the system provides a potential support tool for educators and parents to identify Dyslexia earlier and provide timely educational support.
