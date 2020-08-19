#import numpy.fft as fft
import numpy as np
import h5py as h5
import ctypes
import scipy
from scipy import signal
import matplotlib.pyplot as plt

np.random.seed(123345)

a = np.random.randint(0, 9, (10, 10, 10, 101, 101))
a[:, :, :, 50, :] = np.linspace(0, 50, 101)
a[:, :, :, :, 50] = np.linspace(0, -50, 101)
a[:, :, :, :, 75] = 50 * np.sin(np.linspace(0, -50, 101))

a = a.reshape(10, 10 * 10, 101, 101)

def gaussian_kernel(sigma_x, sigma_y, n_sigma=5.0):
    size_y = int(n_sigma * sigma_y)
    size_x = int(n_sigma * sigma_x)
    x, y = np.mgrid[-size_x:size_x + 1, -size_y:size_y + 1]
    g = np.exp(-(x**2 / (2. * sigma_x**2) + y**2 / (2. * sigma_y**2)))
    return g / g.sum()


def gaussian_smooth(mymap, sigma_x, sigma_y, n_sigma=5.0):
    kernel = gaussian_kernel(sigma_x, sigma_y, n_sigma=n_sigma)
    smoothed_map = signal.fftconvolve(mymap, kernel[np.newaxis, np.newaxis, :, :], mode='same', axes = None)
    #[len(mymap.shape)-2, len(mymap.shape) - 1])
    return smoothed_map


b = gaussian_smooth(a, 10, 3)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(a[0, :, :, 0].T)
ax[0].set_title("Test map")
ax[1].imshow(b[0, :, :, 0].T)
ax[1].set_title("Smoothed")
plt.savefig("test_smoothed_map.png")
plt.show()