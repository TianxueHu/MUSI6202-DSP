import numpy as np

def generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    t = np.linspace(0, length_secs-1/sampling_rate_Hz, sampling_rate_Hz * length_secs)
    x = amplitude * np.sin(2 * phase_radians * frequency_Hz * t)
    return t, x 

if __name__ == '__main__':
    t, x = generateSinusoidal(amplitude=1.0, sampling_rate_Hz = 44100, frequency_Hz=400, length_secs=0.5, phase_radians=np.pi/2)
    print(t,x)