
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