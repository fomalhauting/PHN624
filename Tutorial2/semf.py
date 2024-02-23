import numpy as np

def get_coef(A, Z):
    a1 = A
    a2 = -A**(2/3)
    a3 = -(A - 2 * Z)**2 / A
    a4 = -(Z**2) / A**(1/3)
    a5 = 0

    N = A - Z
    if((N % 2) == 0 and (Z % 2) == 0):
        a5 = 1 / A ** (3/4)
    elif(N % 2 and Z % 2):
        a5 = -1 / A ** (3/4)

    return np.array([a1, a2, a3, a4, a5])

# Coefficients of the linear equations
A = np.array([get_coef(10, 4) , get_coef(14, 6) , get_coef(18, 8) , get_coef(26, 12)  , get_coef(30, 14) ])
B = np.array([6.498 * 10, 7.520 * 14, 7.767 * 18, 8.334 * 26, 8.521 * 30]) 
B = B.reshape(-1, 1)

# Solve the system of linear equations
solution = np.linalg.solve(A, B)

# Extract the coefficients
a_v, a_s, a_a, a_c, a_p = solution

# Function to calculate the binding energy per nucleon
def BAZ(A, Z):
    N = A - Z
    delta = 0
    if(N % 2 == 0 and Z % 2 == 0):
        delta = a_p * 1 / A ** (3/4)
    elif(N % 2 and Z % 2):
        delta = -a_p * 1 / A ** (3/4)
    return a_v * A - a_s * A**(2/3) - a_c * Z **2 / A**(1/3) - a_a * (A-2*Z)**2/A + delta

# Calculate binding energy per nucleon for different nuclei
BAZ(10, 4), BAZ(14, 6), BAZ(18, 8), BAZ(26, 12), BAZ(30, 14)

# SEMF
'''
EB = avA − as(A^2/3) − aA(A − 2Z)^2/A − ac(Z^2)/(A^1/3) + δ(A, Z)

δ(A, Z) = ap/(A^3/4) → N, Z even
0 → A odd
−ap/(A^3/4) → N, Z odd

import numpy as np
import math

# EB = av*A − as*(A^2/3) − aA*((A-2*Z)^2)/A − ac*(Z^2)/(A^1/3) + ap/(A^3/4)

# be - a = 10, z = 4
b1 = 10
b2 = - math.pow(10,2/3)
b3 = - math.pow(10-(2*4),2)/10
b4 = - math.pow(4,2)/math.pow(10,1/3)
b5 = 1/math.pow(10,3/4)

# c - a = 14, z = 6
c1 = 14
c2 = - math.pow(14,2/3)
c3 = - math.pow(14-(2*6),2)/14
c4 = - math.pow(6,2)/math.pow(14,1/3)
c5 = 1/math.pow(14,3/4)

# o - a = 18, z = 8
o1 = 18
o2 = - math.pow(18,2/3)
o3 = - math.pow(18-(2*8),2)/18
o4 = - math.pow(8,2)/math.pow(18,1/3)
o5 = 1/math.pow(18,3/4)

# mg - a = 26, z = 12
m1 = 26
m2 = - math.pow(26,2/3)
m3 = - math.pow(26-(2*12),2)/26
m4 = - math.pow(12,2)/math.pow(26,1/3)
m5 = 1/math.pow(26,3/4)

# si - a = 30, z = 14
s1 = 30
s2 = - math.pow(30,2/3)
s3 = - math.pow(30-(2*14),2)/30
s4 = - math.pow(14,2)/math.pow(30,1/3)
s5 = 1/math.pow(30,3/4)

A = np.array([[b1,b2,b3,b4,b5],[c1,c2,c3,c4,c5],[o1,o2,o3,o4,o5],[m1,m2,m3,m4,m5],[s1,s2,s3,s4,s5]])
b = np.array([6.489, 7.520, 7.767, 8.334, 8.521])
val = np.linalg.solve(A,b)
print(val)


import numpy as np
import math

one = 30
two = -math.pow(30,2/3)
three = -math.pow((30-(2*14)),2)/30
four = -math.pow(14, 2)/math.pow(30, 1/3)
five = 1/math.pow(30, 3/4)

print(one, two, three, four, five)


A = np.array([[10, -4.641588833612778, -0.4, -7.426542133780446, 0.17782794100389226], [14, -5.808785733563703, -0.2857142857142857, -14.936877600592384, 0.1381668871619764],
 [18, -6.868285455319991, -0.2222222222222222, -24.420570507804417, 0.11443150799483988], [26, -8.776382955329126, -0.15384615384615385, -48.60765944489979, 0.08685003324435482],
 [30, -9.654893846056297, -0.13333333333333333, -63.07863979423448, 0.07801157731069054]])
b = np.array([6.489, 7.520, 7.767, 8.334, 8.521])
z = np.linalg.solve(A,b)
print(z)
'''
