from scipy.signal import convolve
from scipy.io import wavfile
from scipy.io.wavfile import read as wavread
import numpy as np
import os
from Q1 import myTimeConv
import time


def CompareConv(x, h):
 
    start = time.process_time()
    y_my = myTimeConv(x, h)
    end_my = time.process_time()
    y_sci = convolve(x, h)
    end_sci = time.process_time()
    time = [end_my - start, end_sci - end_my]


    m = np.mean(y_my[:, None] - y_sci)
    mabs = np.mean(np.abs(y_my[:, None] - y_sci))
    stdev = np.std(y_my[:, None] - y_sci)
    return m, mabs, stdev, np.asarray(time)



def loadSoundFile(filename):
    '''
    a python function x = loadSoundFile(filename) that takes a string and outputs 
    a numpy array of floats - if the file is multichannel you should grab just the left channel.
    '''
    _, audio = wavread(filename)

    if audio.dtype == 'float32':
        x = audio
    else:
        if audio.dtype == 'uint8':
            nbits = 8
        elif audio.dtype == 'int16':
            nbits = 16
        elif audio.dtype == 'int32':
            nbits = 32

        x = audio / float(2**(nbits - 1))

    if audio.dtype == 'uint8':
        x = x - 1.
    
    # take left channel if stereo
    try:
        if x.shape[1] == 2:
            x = x[:,0]
    except:
        pass

    return np.asarray(x)


if __name__ == '__main__':
    cur_dir = os.getcwd()
    xp = "assignment2/piano.wav"
    xpp = os.path.join(cur_dir, xp)
    hp = "assignment2/impulse-response.wav"
    hpp = os.path.join(cur_dir, hp)

    x = loadSoundFile(xpp)
    h = loadSoundFile(hpp)

    m, mabs, stdev, time = CompareConv(x, h)