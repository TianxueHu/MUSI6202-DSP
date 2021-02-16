import numpy as np
import matplotlib.pyplot as plt

def generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    samples = int(sampling_rate_Hz * length_secs)
    t = np.arange(0, (samples+1)/sampling_rate_Hz, 1/sampling_rate_Hz)
    # t = t[:-1] # remove end point
    x = amplitude * np.sin(2 * np.pi * frequency_Hz * t + phase_radians)
    return t, x 

if __name__ == '__main__':
    t, x = generateSinusoidal(amplitude=1.0, sampling_rate_Hz = 44100, \
        frequency_Hz=400, length_secs=0.5, phase_radians=np.pi/2)
    plot_samples = int(44100 * 0.005)
    plot_sin_t = t[:plot_samples]
    plot_sin_x = x[:plot_samples]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(plot_sin_t, plot_sin_x)
    ax.set_title("Generate Sinusoidal")
    ax.set_xlabel("Time in secs")
    ax.set_ylabel("Amplitude")
    #plt.show()
    #plt.savefig('results/q1-generateSinusoidal.png')