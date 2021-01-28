from question_one import crossCorr, loadSoundFile
from scipy.signal import find_peaks
from scipy.io.wavfile import read as wavread
import os



def findSnarePosition(snareFilename, drumloopFilename):
    '''
    Using the correlation, write a function pos = findSnarePosition(snareFilename, drumloopFilename) 
    that takes the string filenames for the snare and drumloop and outputs a regular python list of 
    sample positions of the best guess for the snare position in the drumloop
    '''
    snare = loadSoundFile(snareFilename)
    drum = loadSoundFile(drumloopFilename)

    z = crossCorr(drum, snare)
    peak_indices = find_peaks(z, threshold = 50)

    ## find position in drum loop file (in seconds)
    # total duration of drum loop file in seconds
    fs, audio = wavread(drumloopFilename)
    duration = len(audio) / float(fs)
    # find corresponding position of peak indices in the drum loop file
    output = []
    snare_length = snare.shape[0]
    drum_length = drum.shape[0]
    for idx in peak_indices[0]:
        sec = duration * (idx-snare_length) / drum_length
        output.append(sec)

    return output 


if __name__ == '__main__':
    cur_dir = os.getcwd()
    drumloopFile = "assignment1/drum_loop.wav"
    drumloopFile_path = os.path.join(cur_dir, drumloopFile)
    snareFile = "assignment1/snare.wav"
    snareFile_path = os.path.join(cur_dir, snareFile)

    snare_location = findSnarePosition(snareFile_path, drumloopFile_path)
    '''
    # write file 
    with open('02-snareLocation.txt', 'w') as f:
        for item in  snare_location:
            f.write("%s\n" % item)
    '''