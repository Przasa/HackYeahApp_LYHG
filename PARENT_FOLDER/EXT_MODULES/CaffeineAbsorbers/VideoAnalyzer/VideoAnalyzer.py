import cv2
import numpy as np
# from GUI import play_song
from HeartBeatDetector.ImageFilter import ImageFilter
from matplotlib import pyplot as plt

img_filter = ImageFilter(300)


class ForeheadRecorder:
    def __init__(self, forehead_width, forehead_height):
        self.forehead_width = forehead_width
        self.forehead_height = forehead_height

        self.cap = cv2.VideoCapture(0)  # 0 for the default camera
        # If you want to process a video file:
        # cap = cv2.VideoCapture('video_file.mp4')
        hb_signal = None
        first_update = True

        # Initialize the face cascade classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Check if the classifier was loaded correctly
        if face_cascade.empty():
            print("Error: Could not load face cascade classifier.")
        else:
            print("Face cascade classifier loaded successfully.")

    def record_video(self):


        # Read a frame from the camera
        ret, frame = self.cap.read()
        return ret, frame

