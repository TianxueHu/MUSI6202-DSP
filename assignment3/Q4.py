import numpy as np
from numpy.fft import fft
from Q2 import generateSquare
from Q3 import computeSpectrum
import matplotlib.pyplot as plt


def generateBlocks(x, sample_rate_Hz, block_size, hop_size):
    numBlocks = int(np.ceil(x.shape[0] / hop_size))
    X = np.zeros([numBlocks, block_size])
    t = (np.arange(0, numBlocks) * hop_size) / sample_rate_Hz

    x = np.concatenate((x, np.zeros(block_size)),axis=0)

    for n in range(0, numBlocks):
        i_start = n * hop_size
        i_stop = np.min([x.size - 1, i_start + block_size - 1])
        X[n][np.arange(0,block_size)] = x[np.arange(i_start, i_stop + 1)]
    X = np.transpose(X)
    return t, X


def mySpecgram(x, block_size, hop_size, sampling_rate_Hz, window_type):
    time_vector, X = generateBlocks(x, sampling_rate_Hz, block_size, hop_size)
    print(X.shape)

    if window_type == "hann":
        window = np.hanning(block_size).reshape(block_size, 1)
        print(window.shape)
        X = X * window
    
    
    return freq_vector, time_vector, magnitude_spectrogram
    


if __name__ == '__main__':

    t_sq, x_sq = generateSquare(amplitude=1.0, sampling_rate_Hz = 44100, \
        frequency_Hz=400, length_secs=0.5, phase_radians=0)

    mySpecgram(x_sq, block_size=2048, hop_size=1024, sampling_rate_Hz=44100, window_type='rect')
    mySpecgram(x_sq, block_size=2048, hop_size=1024, sampling_rate_Hz=44100, window_type='hann')