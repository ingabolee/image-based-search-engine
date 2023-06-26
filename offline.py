import codecs
from PIL import Image
from pathlib import Path
import numpy as np
import flask
import json
from feature_extractor import FeatureExtractor

if __name__ == '__main__':
    fe = FeatureExtractor()

    for img_path in sorted(Path("D:/ImageSearchengine/static/image").glob("*.jpg")):
        #print(img_path)
        # Extract deep features here

        feature = fe.extract(img=Image.open(img_path)).tolist()
        #print(type(feature), feature.shape)
        print(type(feature))
        
    

        feature_path = Path("D:/ImageSearchengine/static/feature") / (img_path.stem + ".json")
        print(feature_path)

        # Save the features
        #np.save(feature_path,feature) 
        json.dump(feature,codecs.open(feature_path,'w'))

    for img_path in sorted(Path("D:/ImageSearchengine/static/image").glob("*.jpeg")):
        #print(img_path)
        # Extract deep features here

        feature = fe.extract(img=Image.open(img_path)).tolist()
        #print(type(feature), feature.shape)
        print(type(feature))
        
    

        feature_path = Path("D:/ImageSearchengine/static/feature") / (img_path.stem + ".json")
        print(feature_path)

        # Save the features
        #np.save(feature_path,feature) 
        json.dump(feature,codecs.open(feature_path,'w')) 

    