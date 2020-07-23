import numpy as np
import h5py as h5
import ctypes

"""
a = np.arange(6 * 6 * 6 * 6 * 6)
a = a.reshape(6, 6, 6, 6, 6)

num = 2
n0, n1, n2, n3, n4 = a.shape 
m3, m4 = int(n3 / num), int(n4 / num)
b = np.zeros((n0, n1, n2, m3, m4))

for q in range(n0):
    for h in range(n1):
        for p in range(n2):
            for i in range(m3):
                for j in range(m4):
                    for k in range(i * num, (i + 1)* num):
                        for l in range(j * num, (j + 1) * num):
                            b[q, h, p, i, j] += a[q, h, p, k, l]
                                
print("first")
print(a[0, 0, 0, :, :])
print(b[0, 0, 0, :, :]) 

m_h = np.arange(6 * 6 * 6 * 6 * 6)
m_h = m_h.reshape(6, 6, 6, 6, 6).astype(ctypes.c_float)

n_h = np.arange(6 * 6 * 6 * 6 * 6)
n_h = m_h.reshape(6, 6, 6, 6, 6).astype(ctypes.c_int)

r_h = np.arange(6 * 6 * 6 * 6 * 6)
r_h = m_h.reshape(6, 6, 6, 6, 6).astype(ctypes.c_float)



num = int(3)
n0, n1, n2, n3, n4 = m_h.shape
N3, N4 = int(n3 / num), int(n4 / num)

m_l = np.zeros((n0, n1, n2, N3, N4), dtype = ctypes.c_float)
n_l = np.zeros((n0, n1, n2, N3, N4), dtype = ctypes.c_int)
r_l = np.zeros((n0, n1, n2, N3, N4), dtype = ctypes.c_float)

maputilslib = ctypes.cdll.LoadLibrary("maputilslib.so.1")  # Load shared library

float32_array5 = np.ctypeslib.ndpointer(dtype=ctypes.c_float, ndim=5, flags="contiguous")
int32_array5 = np.ctypeslib.ndpointer(dtype=ctypes.c_int, ndim=5, flags="contiguous")
maputilslib.dgrade5D.argtypes = [float32_array5, int32_array5, float32_array5,
                                 float32_array5, int32_array5, float32_array5,
                                 ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                 ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                 ctypes.c_int, ctypes.c_int]
maputilslib.dgrade5D(m_h, n_h, r_h,
                     m_l, n_l, r_l,
                     n0, n1, n2,
                     n3, n4, N3, N4, num)
print("second")
print(n_h[1, 2, 3, :, :])
print(n_l[1, 2, 3, :, :])
#print(np.allclose(n_h, a))
#print(np.allclose(n_l, b))
"""

a = np.arange(6 * 6 * 6 * 6 * 6 * 6)
a = a.reshape(6, 6, 6, 6, 6, 6)

num = 2
n0, n1, n2, n3, n4, n5 = a.shape 
N3 = int(n3 / num)
b = np.zeros((n0, n1, n2, N3, n4, n5))

for q in range(n0):
    for p in range(n1):
        for k in range(n2):
            for l in range(N3):
                for h in range(l * num, (l + 1)* num):
                    for i in range(n4):
                        for j in range(n5):
                            b[q, p, k, l, i, j] += a[q, p, k, h, i, j]

print(a.shape)
print(b.shape)
print(a[0, 0, 0, 0, :, :], "\n")
print(a[0, 0, 0, 1, :, :], "\n")
print(b[0, 0, 0, 0, :, :])



m_h = np.arange(6 * 6 * 6 * 6 * 6 * 6)
m_h = m_h.reshape(6, 6, 6, 6, 6, 6).astype(ctypes.c_float)

n_h = np.arange(6 * 6 * 6 * 6 * 6 * 6)
n_h = m_h.reshape(6, 6, 6, 6, 6, 6).astype(ctypes.c_int)

r_h = np.arange(6 * 6 * 6 * 6 * 6 * 6)
r_h = m_h.reshape(6, 6, 6, 6, 6, 6).astype(ctypes.c_float)

num = int(2)
n0, n1, n2, n3, n4, n5 = m_h.shape
N3 = int(n3 / num)

m_l = np.zeros((n0, n1, n2, N3, n4, n5), dtype = ctypes.c_float)
n_l = np.zeros((n0, n1, n2, N3, n4, n5), dtype = ctypes.c_int)
r_l = np.zeros((n0, n1, n2, N3, n4, n5), dtype = ctypes.c_float)


maputilslib = ctypes.cdll.LoadLibrary("maputilslib.so.1")  # Load shared library

float32_array6 = np.ctypeslib.ndpointer(dtype=ctypes.c_float, ndim=6, flags="contiguous")
int32_array6 = np.ctypeslib.ndpointer(dtype=ctypes.c_int, ndim=6, flags="contiguous")
maputilslib.dgradeZ6D.argtypes = [float32_array6, int32_array6, float32_array6,
                                  float32_array6, int32_array6, float32_array6,
                                  ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int]

maputilslib.dgradeZ6D(m_h, n_h, r_h,
                      m_l, n_l, r_l,
                      n0,  n1, n2,
                      n3,  n4, n5,
                      N3, num)

print(np.allclose(a, n_h))
print(np.allclose(b, n_l))

