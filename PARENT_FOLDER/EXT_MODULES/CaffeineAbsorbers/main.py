import cv2
import numpy as np
from matplotlib import pyplot as plt

from EXT_MODULES.CaffeineAbsorbers.PlotInTime import *
from EXT_MODULES.CaffeineAbsorbers.HeartBeatDetector.ImageFilter import ImageFilter
from EXT_MODULES.CaffeineAbsorbers.FourierAnalysis.Fourier import FourierAnalysis
from EXT_MODULES.CaffeineAbsorbers.ForeheadRecorder.ForeheadRecorder import  ForeheadRecorder


def main_algo():
    aa = ForeheadRecorder(85, 50)
    aa.record_video()


if __name__ == "__main__":
    main_algo()
