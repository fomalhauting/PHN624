# ke and pe

import numpy as np 

def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

def hermite(x, n):
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * hermite(x, n - 1) - 2 * (n - 1) * hermite(x, n - 2)

def psi(x, n):
    s = (np.exp(-(x * x) / 2) * hermite(x, n)) / (np.sqrt(2 ** n * fact(n)) * (np.pi ** (1 / 4)))
    return s

def differentiate(n, x):
    if n == 0:
        return psi(x, 0) * (x ** 2 - 1)
    elif n == 1:
        return -1 * (8 ** 0.5) * x * psi(x, 0) + (x ** 2 - 1) * (psi(x, 1))
    else:
        return 2 * np.sqrt(n * (n - 1)) * psi(x, n - 2) - np.sqrt(8 * n) * x * psi(x, n - 1) + (x ** 2 - 1) * psi(x, n)

def integrate(n, x0, xn, f):
    del_x = (xn - x0) / n
    I1 = []
    I2 = []
    I3 = []
    for i in range(0, n + 1):
        if i == 0 or i == n:
            I1.append(f(x0 + (i * del_x)))
        elif i % 2 != 0:
            I2.append(4 * f(x0 + (i * del_x)))
        else:
            I3.append(2 * f(x0 + (i * del_x)))
    I = (del_x / 3) * (np.sum(I1) + np.sum(I2) + np.sum(I3))
    return I

KE = np.zeros([5, 5])

for n in range(0, 5):
    for m in range(0, 5):
        c = integrate(100, -10, 10, lambda x: differentiate(m, x) * psi(x, n))
        KE[n][m] = round(-c / 2, 4)

PE = np.zeros([5, 5])
for n in range(0, 5):
    for m in range(0, 5):
        c = integrate(100, -10, 10, lambda x: psi(x, n) * x * x * psi(x, m))
        PE[n][m] = round(c / 2, 4)

tolerance = 1e-10
KE[abs(KE) < tolerance] = 0
PE[abs(PE) < tolerance] = 0

print(KE + PE)
