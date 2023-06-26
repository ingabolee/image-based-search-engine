from fileinput import filename
import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
import flask
import json
import codecs
from flask import Flask, request, render_template
from pathlib import Path
import base64
import glob

app = Flask(__name__)


# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path(r"D:/ImageSearchengine/static/feature").glob("*.json"):
    obj_text=codecs.open(feature_path,'r').read()
    features.append(json.loads(obj_text))
    img_paths.append(Path(r"D:/ImageSearchengine/static/image") / (feature_path.stem + ".jpg"))

features = np.array(features)


@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        image_path = "D:\\ImageSearchengine\\static\\img\\"
        data = request.get_json(force=True)
        filetype = data['type']
        input1 = data['data']
        image = base64.b64decode(input1)

        # Save query image
        if filetype == "jpg":
            filename = image_path +"image.jpg"
            with open(filename, 'wb') as o:
                o.write(image)
            fi = glob.glob(filename)[0]
            im = Image.open(fi)
            im = im.convert('RGB')
            im.save('_'  +".jpg")#image_path + 

        elif filetype == "jpeg":
            filename = image_path +"image.jpeg"
            with open(filename, 'wb') as o:
                o.write(image)
            fi = glob.glob(filename)[0]
            im = Image.open(fi)
            im = im.convert('RGB')
            im.save('_'  +".jpeg")#image_path + 

        elif filetype == "png":
            filename = image_path +"image.png"
            with open(filename, 'wb') as o:
                o.write(image)
            fi = glob.glob(filename)[0]
            im = Image.open(fi)
            im = im.convert('RGB')
            im.save('_'  +".png")#image_path + 


        # Run search
        query = fe.extract(im)
        dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
        ids = np.argsort(dists)[:30]  # Top 30 results
        #scores = [(dists[id], img_paths[id]) for id in ids]
        scores = [id for id in ids]

        print(dists)
        

        #return render_template('index.html',query_path=uploaded_img_path,scores=scores)
        #return flask.jsonify({"dist_id": [str(dists[id]) for id in ids], "paths": [str(img_paths[id]) for id in ids]})
        return flask.jsonify(str(scores))
    else:
        #return render_template("index.html")
        return None

if __name__== "__main__":
    app.run(debug=True)