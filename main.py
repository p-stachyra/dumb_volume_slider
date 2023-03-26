import tkinter as tk
import pygame

from PIL import ImageTk, Image

from Interface import Interface

AUDIO_DIR = "data"


def main():
    Interface(audio_path=AUDIO_DIR)



if __name__ == '__main__':
    main()
