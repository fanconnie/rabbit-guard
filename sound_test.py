import sys
import pygame as pg
import os
import time


def play_sound(sound_file):
    clock = pg.time.Clock()
    try:
        pg.mixer.init()
        pg.mixer.music.load(sound_file)
        print("Music file {} loaded!".format(sound_file))
    except pg.error:
        print("File {} not found! {}".fo