##  anisotropic harmonic oscillator


import numpy as np
import matplotlib.pyplot as plt

# part 1

delta = np.linspace(-1,1, 100)
plt.figure(figsize=(8,8))
plt.axvline(x=0, c='k', linewidth=0.5)
plt.ylim(0.5, 7.5)
plt.xlim(-1,1)
plt.title("Anisotropic Harmonic Oscillator")

for N in range(0,7):
    E0 = N + 1.5
    for nz in range (N, -1, -1):
        nrho = N - nz
        E = (E0 - delta*(2*nz-nrho)/3)
        plt.plot(delta, E, linewidth=1.5, label={E0})
plt.xlabel('Deformation')
plt.ylabel('Energy')


# part 2

def calculate_f(delta):
    """Calculates the f function."""
    return ((1 + (2/3) * delta) ** 2 * (1 - (4/3) * delta)) ** (-1/6)

def calculate_hbar_omega_0(A, delta):
    """Calculates hbar * omega_0"""
    return 41 * A ** (-1/3) * calculate_f(delta)

delta = np.arange(-1, 0.75, 0.01)
plt.figure(figsize=(8,8))
plt.axvline(x=0, c='k', linewidth=0.5)
# plt.ylim(0.5, 7.5)
# plt.xlim(-1,1)
plt.title("Anisotropic Harmonic Oscillator")

for N in range(0,7):
    E0 = N + 1.5
    for nz in range (N, -1, -1):
        nrho = N - nz
        E = (E0 - delta*(2*nz-nrho)/3)* calculate_hbar_omega_0(80, delta)
        plt.plot(delta, E, linewidth=1.5, label={E0})
plt.xlabel('Deformation')
plt.ylabel('Energy')
