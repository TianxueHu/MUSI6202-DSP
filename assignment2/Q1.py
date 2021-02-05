
import numpy as np
import matplotlib.pyplot as plt

'''
Q1-2 Answer: If the length of 'x' is 200 and the length of 'h' is 100, y is of length 300
'''

def myTimeConv(x, h):
    '''
    Write a python function y = myTimeConv(x,h) that computes the sample by sample time domain convolution of two signals. 
    'x' and 'h' are the signal and impulse response respectively and must be NumPy arrays. 
    'y' is the convolution output and also must be a NumPy array (single channel signals only). 
    '''
    nh = h.shape[0]
    nx = x.shape[0]
    npad = nh//2
    pad = np.zeros((npad))
    x_pad = np.hstack([pad, x, pad])

    y = []
    A = [] 
    for n in range(nx):
        x_tmp= x_pad[n:n+nh]
        A.append(x_tmp)
        #y.append(list(x_tmp*h[::-1]))
        y.append(list(x_tmp*h))
    y = np.array(y)
    y = y.sum(1)
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

    print(np.convolve(x,h))
    y = myTimeConv(x,h)
    print(y)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(y)
    ax.set_title("Convolution of 2 Signals")
    ax.set_xlabel("time")
    ax.set_ylabel("amplitude")
    plt.show()
