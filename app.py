from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import cv2

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
