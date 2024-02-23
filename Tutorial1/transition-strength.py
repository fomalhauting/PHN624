# transition strength

import numpy as np
import math

def factorial(x):
    f = 1
    for i in range(1, int(x)+1):
        f = i*f
    return f

def cgcoeff(j1, j2, j, m1, m2, m):
    if m1+m2 != m or j < abs(j1-j2) or j > j1+j2 or j+m < 0 or j-m < 0:
        return 0
    t1 = math.sqrt((2*j+1) * factorial(j1+j2-j) * factorial(j+j1-j2) * factorial(j+j2-j1) / factorial(j1+j2+j+1))
    t2 = math.sqrt(factorial(j1+m1) * factorial(j1-m1) * factorial(j2+m2) * factorial(j2-m2) * factorial(j+m) * factorial(j-m))
    smax = int(min(j1+j2-j, j1-m1, j2+m2)) + 1
    smin = int(-min(j-j2+m1, j-j1-m2, 0))
    t3 = 0
    for s in range(smin, smax):
        t3 += np.power(-1,s) / (factorial(s) * factorial(j1+j2-j-s) * factorial(j1-m1-s) * factorial(j2+m2-s) * factorial(j-j2+m1+s) * factorial(j-j1-m2+s))
    c = (-1)**(j1-j2-m)/np.sqrt(2*j+1)
    return c*t1*t2*t3

# Calculate B(E2) values for the two transitions
BE2_1 = ((5/(16*np.pi)) * (224**2) * (cgcoeff(17/2,2,13/2,5/2,0,5/2))**2) 
BE2_2 = ((5/(16*np.pi)) * (202**2) * (cgcoeff(17/2,2,13/2,5/2,0,5/2))**2) 

print(BE2_1)
print(BE2_2)
