import cv2
import numpy as np
import matplotlib.pyplot as plt


class FourierAnalysis:
    def __init__(self, min_range=0.80, max_range=3.4, fs=20):
        self.abs_fft_result = None
        self.frequencies = None
        self.min_range = min_range
        self.max_range = max_range
        self.fs = fs

    def perform_fourier(self, signal_in):
        fft_result = np.fft.fft(signal_in) / len(signal_in)
        fft_result = fft_result[range(int(len(signal_in) / 2))] * 2  # Exclude sampling frequency
        tpCount = len(signal_in)
        values = np.arange(int(tpCount / 2))
        timePeriod = tpCount / self.fs
        self.frequencies = values / timePeriod
        self.abs_fft_result = np.abs(fft_result)

    def get_heart_rate_frequency(self):
        range_freq = np.where(np.logical_and(self.frequencies >= self.min_range, self.frequencies <= self.max_range))
        frequencies_indicies_in_range = np.argmax(self.abs_fft_result[range_freq])
        hz_max = self.frequencies[frequencies_indicies_in_range + range_freq[0][0]]
        return hz_max

    def run(self, signal_in):
        self.perform_fourier(signal_in)
        return self.get_heart_rate_frequency()


def perform_fourier(signal_in):
    # Create a sample 1D signal
    fs = 20  # Sampling frequency (Hz)
    t = np.linspace(0, 15, fs * 15, endpoint=False)  # Time vector from 0 to 1 second

    # Perform the 1D FFT
    fft_result = np.fft.fft(signal_in) / len(signal_in)
    fft_result = fft_result[range(int(len(signal_in) / 2))] * 2  # Exclude sampling frequency
    tpCount = len(signal_in)
    values = np.arange(int(tpCount / 2))
    timePeriod = tpCount / fs
    frequencies = values / timePeriod

    freq_mask = np.where((frequencies >= 6) & (frequencies <= 8))
    range_freq = np.where(np.logical_and(frequencies >= 3, frequencies <= 5))

    fiucioszek = np.abs(fft_result)
    a = np.argmax(fiucioszek[range_freq])
    b = frequencies[a]
    hz_max = frequencies[a + range_freq[0][0]]
    test = fiucioszek[hz_max]

    # Plot the original signal and its FFT
    plt.figure(figsize=(12, 4))

    plt.subplot(121)
    plt.plot(t, signal_in)
    plt.title('Original Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('signal3')

    plt.subplot(122)
    plt.plot(frequencies, fiucioszek)
    plt.title('FFT of Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')

    plt.tight_layout()
    plt.show()

#
# # Frequency of the signals
# signal1Frequency = 4
# signal2Frequency = 7
# fs = 20  # Sampling frequency (Hz)
# time = np.arange(0, 15, 1 / fs)  # Time vector from 0 to 1 second
# signal1 = np.sin(2 * np.pi * signal1Frequency * time)
# signal2 = np.sin(2 * np.pi * signal2Frequency * time) * 2
# signal3 = signal1 + signal2
# perform_fourier(signal3)
#
# # Create subplot
# figure, axis = plt.subplots(4, 1)
# plt.subplots_adjust(hspace=1)
#
# # Time domain representation for sine wave 1
# axis[0].set_title('Sine wave with a frequency of 4 Hz')
# axis[0].plot(time, signal1)
# axis[0].set_xlabel('Time')
# axis[0].set_ylabel('signal3')
#
# # Time domain representation for sine wave 2
# axis[1].set_title('Sine wave with a frequency of 7 Hz')
# axis[1].plot(time, signal2)
# axis[1].set_xlabel('Time')
# axis[1].set_ylabel('signal3')
#
# # Time domain representation of the resultant sine wave
# axis[2].set_title('Sine wave with multiple frequencies')
# axis[2].plot(time, signal3)
# axis[2].set_xlabel('Time')
# axis[2].set_ylabel('signal3')
#
# # Frequency domain representation
# fourierTransform = np.fft.fft(signal3) / len(signal3)  # Normalize signal3
# fourierTransform = fourierTransform[range(int(len(signal3) / 2))]  # Exclude sampling frequency
# tpCount = len(signal3)
# values = np.arange(int(tpCount / 2))
# timePeriod = tpCount / fs
# frequencies = values / timePeriod
#
# # Frequency domain representation
# axis[3].set_title('Fourier transform depicting the frequency components')
# axis[3].plot(frequencies, abs(fourierTransform))
# axis[3].set_xlabel('Frequency')
# axis[3].set_ylabel('signal3')
#
# plt.show()
#
# plt.show()
