import numpy as np
from numpy.fft import fft, fftfreq
from Q1 import generateSinusoidal
from Q2 import generateSquare
import matplotlib.pyplot as plt


def computeSpectrum(x, sample_rate_Hz):
    sig_len = x.shape[0]
    spectrum = fft(x) / sig_len

    # get length of the non-repeated part
    spec_len = spectrum.shape[0]
    half_len = int(spec_len/2)
   
    f = fftfreq(spectrum.shape[0], 1/sample_rate_Hz)[:half_len]
    XAbs = np.abs(spectrum[:half_len])
    XPhase = np.angle(spectrum[:half_len])
    XRe = spectrum[:half_len].real
    XIm = spectrum[:half_len].imag
    return f, XAbs, XPhase, XRe, XIm


if __name__ == '__main__':
    t_sin, x_sin = generateSinusoidal(amplitude=1.0, sampling_rate_Hz = 44100, \
        frequency_Hz=400, length_secs=0.5, phase_radians=np.pi/2)
    t_sq, x_sq = generateSquare(amplitude=1.0, sampling_rate_Hz = 44100, \
        frequency_Hz=400, length_secs=0.5, phase_radians=0)
    sin_f, sin_x_mag, sin_x_phase, sin_x_re, sin_x_im = computeSpectrum(x_sin, 44100)
    sq_f, sq_x_mag, sq_x_phase, sq_re, sq_x_pim = computeSpectrum(x_sq, 44100)

    fig = plt.figure()
    ax = fig.add_subplot(2,1,1)
    ax.plot(sin_f, sin_x_mag)
    ax.set_title("Magnitude and Phase of a Sin Wave")
    ax.set_xlabel("Frequency in Hz")
    ax.set_ylabel("Magnitude")
    ax = fig.add_subplot(2,1,2)
    ax.plot(sin_f, sin_x_phase)
    ax.set_xlabel("Frequency in Hz")
    ax.set_ylabel("Phase")
    plt.show()
    #plt.savefig('results/q3-sinwave_magphase.png')

    fig = plt.figure()
    ax = fig.add_subplot(2,1,1)
    ax.plot(sq_f, sq_x_mag)
    ax.set_title("Magnitude and Phase of a Square Wave")
    ax.set_xlabel("Frequency in Hz")
    ax.set_ylabel("Magnitude")
    ax = fig.add_subplot(2,1,2)
    ax.plot(sq_f, sq_x_phase)
    ax.set_xlabel("Frequency in Hz")
    ax.set_ylabel("Phase")
    #plt.show()
    #plt.savefig('results/q3-squarewave_magphase.png')