import os
import sys

from Camera import Camera
import cv2

from flask import Response, Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def indexPage():
    return render_template('index.html')


def gen(camera):
    while True:
        try:
            frame = camera.getFrame()
     