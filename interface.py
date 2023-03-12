import numpy as np
import cv2
import imutils
from PIL import Image
import pytesseract
import os
import matplotlib.pyplot as plt

from flask import Flask, request, Response
from read import scan

app = Flask(__name__)

# @app.route("/upload")
# def hello():
#     return "Hello World"
def read(image,data,side):

  image=imutils.resize(image, height = 350)
  image_Trasform2 = cv2.resize(image,(1000,630))
  data = scan (image_Trasform2 , side , data )
  return data

@app.route('/', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # file = request.files['file']
    # Read the image via file.stream
    # img = Image.open(file.stream)
    
    data = {}
    side = 'f'
    data = read(img,data,side)

    # filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config['upload_folder'], filename))
    
if __name__ == "__main__":
    app.run(debug=True) 