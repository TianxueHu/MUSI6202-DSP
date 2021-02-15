import numpy as np
import matplotlib.pyplot as plt
from Q1 import generateSinusoidal

def generateSquare(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    t, _ = generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians)
    x = np.zeros(len(t))

    for i in range(10):
        n = i * 2 + 1 # nth harmonic
        amp = amplitude * 4/(np.pi*n) 
        t, xtmp = generateSinusoidal(amp, sampling_rate_Hz, frequency_Hz * n, length_secs, phase_radians * n)
        x += xtmp
    return t, x


if __name__ == '__main__':
    t, x = generateSquare(amplitude=1.0, sampling_rate_Hz = 44100, \
        frequency_Hz=400, length_secs=0.5, phase_radians=0)
    plot_samples = int(44100 * 0.005)
    plot_sin_t = t[:plot_samples]
    plot_sin_x = x[:plot_samples]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(plot_sin_t, plot_sin_x)
    ax.set_title("Generate Square")
    ax.set_xlabel("Time in secs")
    ax.set_ylabel("Amplitude")
    #plt.show()
    #plt.savefig('results/q2-generateSquare.png')