import os
import sys

from Camera import Camera
import cv2

from flask import Response, Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
d