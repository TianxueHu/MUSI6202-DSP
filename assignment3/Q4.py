import numpy as np
from numpy.fft import fft, fftfreq
from Q1 import generateSinusoidal
from Q2 import generateSquare
from Q3 import computeSpectrum
import matplotlib.pyplot as plt


def generateBlocks(x, sample_rate_Hz, block_size, hop_size):
    numBlocks = math.ceil(x.size / hop_size)
    X = np.zeros([numBlocks, block_size])
    t = (np.arange(0, numBlocks) * hop_size) / sample_rate_Hz

    x = np.concatenate((x, np.zeros(block_size)),axis=0)

    for n in range(0, numBlocks):
        i_start = n * hop_size
        i_stop = np.min([x.size - 1, i_start + block_size - 1])
        X[n][np.arange(0,block_size)] = x[np.arange(i_start, i_stop + 1)]

    return t, X

def mySpecgram(x, block_size, hop_size, sampling_rate_Hz, window_type):
    t, X = generateBlocks(x, sample_rate_Hz, block_size, hop_size)

    if window_type == "hann":
        
    elif window_type = "rect":
