from scipy.io import wavfile
from scipy.signal import correlate
from scipy.io.wavfile import read as wavread
import numpy as np
import matplotlib.pyplot as plt
import os


def crossCorr(x, y): 
    '''
    A python function z = crossCorr(x, y) where x, y and z are numpy arrays of floats.
    input: x,y as numpy arrays
    output: an array
    '''

    return correlate(x, y, "full") 


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
    if x.shape[1] == 2:
        x = x[:,0]

    return np.asarray(x)


if __name__ == '__main__':
    cur_dir = os.getcwd()
    drumloopFile = "assignment1/drum_loop.wav"
    drumloopFile_path = os.path.join(cur_dir, drumloopFile)
    snareFile = "assignment1/snare.wav"
    snareFile_path = os.path.join(cur_dir, snareFile)

    snare = loadSoundFile(snareFile_path)
    drum = loadSoundFile(drumloopFile_path)

    z = crossCorr(drum, snare)
    
    '''
    plt.plot(z)
    plt.show()
    #plt.savefig("01-correlation.png")
    '''
    