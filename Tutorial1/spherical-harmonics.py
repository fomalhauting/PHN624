import numpy as np
from scipy.special import lpmv

def sphericalharmonics(l, m, theta, phi):
    P = lpmv(m, l, np.cos(theta))
    Y = np.sqrt((2*l+1)/(4*np.pi)) * np.sqrt(np.math.factorial(l-m)/np.math.factorial(l+m)) * P * np.exp(1j*m*phi)
    return Y

# define the values of l and m
l = 2
m = 1

theta = np.linspace(0, np.pi, 50)
phi = np.linspace(-np.pi, np.pi, 100)

theta_mesh, phi_mesh = np.meshgrid(theta, phi)
Yml = sphericalharmonics(l, m, theta_mesh, phi_mesh)

print(Yml)
