import numpy as np
from helper import *

def cgcoeff(j1, j2, j, m1, m2, m):
    if m1+m2 != m or j < abs(j1-j2) or j > j1+j2 or j+m < 0 or j-m < 0:
        return 0
    t1 = np.sqrt((2*j+1) * np.math.factorial(j1+j2-j) * np.math.factorial(j+j1-j2) * np.math.factorial(j+j2-j1) / np.math.factorial(j1+j2+j+1))
    t2 = np.sqrt(np.math.factorial(j1+m1) * np.math.factorial(j1-m1) * np.math.factorial(j2+m2) * np.math.factorial(j2-m2) * np.math.factorial(j+m) * np.math.factorial(j-m))
    smax = min(j1+j2-j, j1-m1, j2+m2) + 1
    smin = -min(j-j2+m1, j-j1-m2, 0)
    t3 = 0
    for s in range(smin, smax):
        t3 += np.power(-1,s) / (np.math.factorial(s) * np.math.factorial(j1+j2-j-s) * np.math.factorial(j1-m1-s) * np.math.factorial(j2+m2-s) * np.math.factorial(j-j2+m1+s) * np.math.factorial(j-j1-m2+s))
    c = (-1)**(j1-j2-M)/np.sqrt(2*J+1)
    return c*t1*t2*t3

j1 = 1
j2 = 2
J = 2
m1 = 1
m2 = -1
M = 0

print(cgcoeff(j1,j2,J,m1,m2,M))
