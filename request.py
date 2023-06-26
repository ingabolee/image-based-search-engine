from fileinput import filename
import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        file = request.files["data"]
        

        # Save query image
        img = Image.open(file.stream)
        uploaded_img_path = r"D:/ImageSearchengine/static/image/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)
        return("Image is being saved")


if __name__== "__main__":
    app.run(debug=True)