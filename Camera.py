
import base64
import io
import os

import cv2
import requests
import pygame as pg
from PIL import Image

from config import *
from threading import Thread

import copy


class Camera:
    def __init__(self, source):
        # Video capture
        self.video = cv2.VideoCapture(source)
        self.soundFile = os.getcwd() + os.sep + 'car-honk.mp3'
        self.soundCondition = False
        self.uploadCondition = False
        pg.mixer.init()
        pg.mixer.music.load(self.soundFile)

    def getRawFrame(self):
        # Returns the raw frame
        _, frameToReturn = self.video.read()
        return frameToReturn

    # Frame with annotations
    def getFrameAnnotations(self):
        success, img = self.video.read()
        # Rotate Camera Upside down if needed
        # img = cv2.rotate(img, cv2.ROTATE_180)
        # Resize (while maintaining the aspect ratio) to improve speed and save bandwidth
        height, width, channels = img.shape
        scale = ROBOFLOW_SIZE / max(height, width)
        img = cv2.resize(img, (round(scale * width), round(scale * height)))

        # Encode image to base64 string
        retval, buffer = cv2.imencode('.jpg', img)
        img_str = base64.b64encode(buffer)

        # Get predictions from Roboflow Infer API
        resp = requests.post(infer_url, data=img_str, headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }, stream=True).json()['predictions']

        rawImg = copy.deepcopy(img)
        # Draw all predictions
        respCount = 0
        for prediction in resp:
            if prediction["confidence"] > CONFIDENCE_THRESHOLD:
                respCount += 1
                self.writeOnStream(prediction['x'], prediction['y'], prediction['width'], prediction['height'],
                                   prediction['class'],
                                   img)

        return respCount > 0, img, rawImg, resp

    def getFrame(self):
        sound, img, rawImg, apiResponse = self.getFrameAnnotations()
        # Multithread sound
        if not self.soundCondition and sound:
            self.soundCondition = True
            soundThread = Thread(target=self.playSound)
            soundThread.start()

        # Multithread Active Learning