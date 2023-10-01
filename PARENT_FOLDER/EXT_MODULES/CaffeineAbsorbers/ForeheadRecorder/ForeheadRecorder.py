import cv2
import numpy as np
from EXT_MODULES.CaffeineAbsorbers.PlotInTime import *
# from GUI import play_song
from EXT_MODULES.CaffeineAbsorbers.HeartBeatDetector.ImageFilter import ImageFilter
from EXT_MODULES.CaffeineAbsorbers.FourierAnalysis.Fourier import FourierAnalysis
from matplotlib import pyplot as plt

class ForeheadRecorder:
    def __init__(self, forehead_width, forehead_height):
        self.forehead_width = forehead_width
        self.forehead_height = forehead_height

    def record_video(self):
        img_filter = ImageFilter(300)
        fouier_analyzer = FourierAnalysis()
        cap = cv2.VideoCapture(0)  # 0 for the default camera
        # If you want to process a video file:
        # cap = cv2.VideoCapture('video_file.mp4')
        hb_signal = None
        hb_test = []
        first_update = True

        # Initialize the face cascade classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Check if the classifier was loaded correctly
        if face_cascade.empty():
            print("Error: Could not load face cascade classifier.")
        else:
            print("Face cascade classifier loaded successfully.")
        is_first_sig = True
        signal = None
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            if not ret:
                break  # If the camera is not providing frames, exit the loop

            # Detect faces
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                # Show rectangle around face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle around the face

                # Select a region of interest (e.g., cheek or forehead)
                roi = frame[y:y + h, x:x + w]

                # forehead recognition
                roi_height, roi_width, _ = roi.shape

                x_forehead = round(roi_width / 2 - self.forehead_width / 2)
                y_forehead = round(roi_height * 0.15 - self.forehead_height / 2)

                forehead_region = frame[y + y_forehead:y + y_forehead + self.forehead_height,
                                  x + x_forehead:x + x_forehead + self.forehead_width]

                cv2.imshow('Face', roi)
                cv2.rectangle(roi, (x_forehead, y_forehead),
                              (x_forehead + self.forehead_width, y_forehead + self.forehead_height), (255, 0, 0),
                              2)  # Blue rectangle around the forehead

                # Extract color signal from ROI and perform signal processing
                forehead_region[:, :, 0] = 0  # Set the blue channel to zero (0)
                forehead_region[:, :, 2] = 0  # Set the red channel to zero (0)
                cv2.imshow('Forehead', forehead_region)

                # Calculate heart rate and display it on the frame
                #################################################
                #################################################
                #################################################
                #################################################
                tmp_hb_signal = img_filter.run_algo(forehead_region)

                if tmp_hb_signal is not None:
                    heart_rate = fouier_analyzer.run(tmp_hb_signal)
                    print("heart_rateA: {}".format(heart_rate))
                    hb_test.append(heart_rate)


            cv2.imshow('Heart Rate Detection', frame)
            # Exit the loop if the user presses the 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close the OpenCV windows when done
        plot_vector(signal)
        cap.release()
        cv2.destroyAllWindows()

        plt.figure()
        plt.plot(hb_test)
        plt.show()