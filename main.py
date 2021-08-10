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
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        except Exception as e:
            exceptionType, exceptionObject, exceptionThrowback = sys.exc_info()
            fileName = os.path.split(exceptionThrowback.tb_frame.f_code.co_filename)[1]
            print(exceptionType, fileName, ex