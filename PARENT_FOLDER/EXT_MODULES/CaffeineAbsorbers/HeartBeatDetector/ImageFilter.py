import cv2
import numpy as np
import scipy.signal as signal
import scipy.fftpack as fftpack


class ImageFilter:
    def __init__(self, window_len):
        self.signal = np.zeros((1, 50, 85, 3))
        self.diff = None
        self.window_len = window_len
        self.fp = 20

    def run_algo(self, new_frame):
        hb_sig = None
        self.update_frames(new_frame)
        if self.signal.shape[0] >= self.window_len:
           hb_sig = self.create_hb_signal(0.4,3)

        return hb_sig

    def update_frames(self, new_frame):
        self.add_new_frame(new_frame)
        if self.signal.shape[0] > self.window_len:
            self.delete_last_frame()

    def add_new_frame(self, new_frame):
        tmp_signal = self.signal
        self.signal = np.append(tmp_signal, [new_frame], axis=0)

    def delete_last_frame(self, ):
        self.signal = self.signal[1:, :, :, :]

    def create_hb_signal(self, low, high, levels=3, amplification=20):
        gau_video = ImageFilter.gaussian_video(self.signal, levels=levels)
        filtered_tensor = ImageFilter.temporal_ideal_filter(gau_video, low, high, self.fp)
        amplified_video = ImageFilter.amplify_video(filtered_tensor, amplification=amplification)
        frames = ImageFilter.reconstruct_video(amplified_video, self.signal, levels=3)
        a =  ImageFilter.calculate_median(frames)
        return a

    @staticmethod
    def gaussian_video(video_tensor, levels=3):
        for i in range(0, video_tensor.shape[0]):
            frame = video_tensor[i]
            pyr = ImageFilter.build_gaussian_pyramid(frame, level=levels)
            gaussian_frame = pyr[-1]
            if i == 0:
                vid_data = np.zeros((video_tensor.shape[0], gaussian_frame.shape[0], gaussian_frame.shape[1], 3))

            if vid_data[i].shape != gaussian_frame.shape:
                vid_data[i, :, :, 0] = gaussian_frame
            else:
                vid_data[i] = gaussian_frame
        return vid_data

    @staticmethod
    def build_gaussian_pyramid(src, level=3):
        s = src.copy()
        pyramid = [s]
        for i in range(level):
            s = cv2.pyrDown(s)
            pyramid.append(s)
        return pyramid

    @staticmethod
    def temporal_ideal_filter(tensor, low, high, fps, axis=0):
        fft = fftpack.fft(tensor, axis=axis)
        frequencies = fftpack.fftfreq(tensor.shape[0], d=1.0 / fps)
        bound_low = (np.abs(frequencies - low)).argmin()
        bound_high = (np.abs(frequencies - high)).argmin()
        fft[:bound_low] = 0
        fft[bound_high:-bound_high] = 0
        fft[-bound_low:] = 0
        iff = fftpack.ifft(fft, axis=axis)
        return np.abs(iff)

    @staticmethod
    def amplify_video(gaussian_vid, amplification=50):
        return gaussian_vid * amplification

    @staticmethod
    def reconstruct_video(amp_video, origin_video, levels=3):
        final_video = np.zeros(origin_video.shape)
        for i in range(0, amp_video.shape[0]):
            img = amp_video[i]
            for x in range(levels):
                img = cv2.pyrUp(img)
            final_video[i] = img[:50, :85, :]
        return final_video

    @staticmethod
    def calculate_median(frame):
        return np.median(np.median(frame[:,:,:,1], axis=-1), axis=-1)

