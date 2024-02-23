# spherical harmonics

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    f=1
    for i in range(1,x+1):
        f=i*f
    return f
def df(n):
    if(n%2==0):
        l1=np.arange(2,n+1,2)
        return np.prod(l1)
    elif(n%2!=0):
        l2=np.arange(1,n+1,2)
        return np.prod(l2)
    
    
def associate_legendre(x,l,m):
    if l < abs(m): return x - x

    if m < 0: return (-1) ** abs(m) * f(l - abs(m)) / f(l + abs(m)) * associate_legendre(x, l, abs(m))
    if l == m: return (-1) ** l * df(2 * l - 1) * (1 - x ** 2) ** (l / 2)
    if l == m+1: return x * (2 * m + 1) * associate_legendre(x, m, m)
    return (x * (2 * l - 1) * associate_legendre(x, l-1, m) - (l + m - 1) * associate_legendre(x, l-2, m)) / (l - m)
    
def spherical_harmonic(l,m,theta,phi):
    sh = ((-1)**m) * np.sqrt(((2*l+1)*f(l-m))/(4*np.pi*f(l+m))) * associate_legendre(np.cos(theta),l,m) * np.cos(m*phi)
    return sh

theta, phi  = np.meshgrid(np.linspace(0,np.pi,100),np.linspace(0, 2*np.pi,100))

xyz = np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])


l_value=int(input("Enter l"))
fig = plt.figure(figsize=(10,12 ))
index=0
for l in range(0,l_value+1):
   for m in range(-l,l+1):
        index+=1
        ax= fig.add_subplot(5,4,index, projection='3d')
        plt.title(f"l = {l}, m = {m}")
        Y = np.abs(spherical_harmonic(l, m, theta, phi)) * xyz
        ax.plot_surface(Y[0], Y[1], Y[2])
plt.tight_layout()
plt.show()
