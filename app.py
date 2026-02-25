import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# ---------------------------------
# Flask App Setup
# ---------------------------------
app = Flask(__name__)

# ---------------------------------
# Paths
# ---------------------------------
MODEL_PATH = "models/dyslexia_model_best.h5"
IMG_SIZE = 224   # Change if your model uses a different input size

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------------------------
# Load Model
# ---------------------------------
model = load_model(MODEL_PATH)

# ---------------------------------
# Home Route
# ---------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------------
# Predict Route
# ---------------------------------
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    # Save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Preprocess image
    img = image.load_img(filepath, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
   # Make prediction
    prediction = model.predict(img_array)[0][0]
    print("Prediction value:", prediction)

    if prediction > 0.5:
     result = "Non-Dyslexia"
    else:
     result = "Dyslexia"

    return render_template(
        "index.html",
        prediction=result,
        image_file="uploads/" + file.filename
    )

# ---------------------------------
# Run App
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)