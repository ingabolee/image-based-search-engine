import base64
import numpy as np
import glob
from flask import (
    Flask,
    request,
    render_template,
    send_from_directory,
    url_for,
    jsonify
)

from PIL import Image
app = Flask(__name__)

@app.route('/image_search_engine', methods=["POST"])

def image_search():
    if request.method == "POST":
        image_path = "D:\\ImageSearchengine\\static\\img\\"
        data = request.get_json(force=True)
        filetype = data['type']
        input1 = data['data']
        image = base64.b64decode(input1)


        if filetype == "jpg":
            filename = image_path +"image.jpg"
            with open(filename, 'wb') as o:
                o.write(image)
            fi = glob.glob(filename)[0]
            im = Image.open(fi)
            im = im.convert('RGB')
            im.save( "_"  +".jpg")#image_path+
            #np.save(image_path,im)
            return ("The file is a jpg")


if __name__ == '__main__':
 
    app.run('0.0.0.0', 8000 ,debug=True,threaded=False)