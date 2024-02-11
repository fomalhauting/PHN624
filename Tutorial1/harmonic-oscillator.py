# Ψn(x) = 1/√((2^n)*n!) (mω/πℏ)^1/4 exp (−mωx^2/2ℏ) Hn ((√mω/ℏ)x)
# mω/ℏ = 1
import numpy as np
import matplotlib.pyplot as plt

def hermite(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2*x*hermite(x,n-1) - 2*(n-1)*hermite(x,n-2)

def harmonic(x, n):
    a = 1/(np.sqrt((2**n)*np.math.factorial(n)))
    b = np.exp(-(x**2)/2)
    m = (1/np.math.pi)**(1/4)
    h = hermite(x, n)
    return a*m*b*h

X = np.arange(-5, 5, 0.1)

for n in range(5):
    Psi = harmonic(X, n)
    plt.plot(X, Psi)

plt.show()
