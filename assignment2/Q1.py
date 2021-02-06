
import numpy as np
import matplotlib.pyplot as plt

'''
Q1-2 Answer: If the length of 'x' is 200 and the length of 'h' is 100, y is of length 200 + 100 - 1 = 299
'''

def myTimeConv(x, h):
    '''
    Write a python function y = myTimeConv(x,h) that computes the sample by sample time domain convolution of two signals. 
    'x' and 'h' are the signal and impulse response respectively and must be NumPy arrays. 
    'y' is the convolution output and also must be a NumPy array (single channel signals only). 
    '''
    nh = h.shape[0]
    nx = x.shape[0]

    # init convolve output
    ny = nx + nh -1
    y = np.zeros(ny)
    # flip the impulse
    h = np.flip(h) 
    # pad signal
    x = np.pad(x, nh-1)
    
    for n in range(ny):
        y[n] = np.sum(np.dot(h, x[n:n+nh]))

    return y 



if __name__ == '__main__':
    # Q1-3
    x = np.asarray([1]*200)
    h = []
    for i in range(25):
        h.append(i*1/25)
    h.append(1)
    for i in range(1, 26):
        h.append((25-i)*1/25)
    h = np.asarray(h)

    y = myTimeConv(x,h)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(y)
    ax.set_title("Convolution of 2 Signals")
    ax.set_xlabel("time")
    ax.set_ylabel("amplitude")
    #plt.show()
    #plt.savefig("results/02-convolution.png", format = "png")
