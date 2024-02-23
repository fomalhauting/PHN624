# rutherford

import numpy as np
import matplotlib.pyplot as plt

# Gold nucleus
A_nucleus = 197
Z_nucleus = 79
# Alpha particle
A_alpha = 4
Z_alpha = 2

R_T = 1.2 * (A_nucleus**(1/3))  # in fm
e_sq = 1.44  # MeV-fm

m_n = 939.5654133  # MeV/c_sq
m_p = 938.2720813  # MeV/c_sq
m_alpha = 2 * (m_n + m_p)

E_alpha = 5.0  # MeV
v_alpha = np.sqrt(2 * E_alpha / m_alpha)

def f1(t, z1, z2, z3, z4):
    return z2

def f2(t, z1, z2, z3, z4):
    rR = np.sqrt(z1**2 + z3**2)
    r = max(rR, R_T)
    return Z_nucleus * Z_alpha * e_sq * z1 / (m_alpha * (r**3))

def f3(t, z1, z2, z3, z4):
    return z4

def f4(t, z1, z2, z3, z4):
    rR = np.sqrt(z1**2 + z3**2)
    r = max(rR, R_T)
    return Z_nucleus * Z_alpha * e_sq * z3 / (m_alpha * (r**3))

# RK4 solver:
def RK4solver(b):
    z1_0 = -100.0  # in femtometers
    z2_0 = v_alpha
    z4_0 = 0.0
    t0 = 0.0
    tf = 10000.0  # in fm/c
    n = 10000
    h = (tf - t0) / n
    Z1 = []
    Z2 = []
    Z3 = []
    Z4 = []
    t = []

    Z1.append(z1_0)
    Z2.append(z2_0)
    Z3.append(b)
    Z4.append(z4_0)
    t.append(t0)

    for i in range(n):
        k1 = h * f1(t[i], Z1[i], Z2[i], Z3[i], Z4[i])
        l1 = h * f2(t[i], Z1[i], Z2[i], Z3[i], Z4[i])
        m1 = h * f3(t[i], Z1[i], Z2[i], Z3[i], Z4[i])
        n1 = h * f4(t[i], Z1[i], Z2[i], Z3[i], Z4[i])

        k2 = h * f1(t[i] + h/2, Z1[i] + k1/2, Z2[i] + l1/2, Z3[i] + m1/2, Z4[i] + n1/2)
        l2 = h * f2(t[i] + h/2, Z1[i] + k1/2, Z2[i] + l1/2, Z3[i] + m1/2, Z4[i] + n1/2)
        m2 = h * f3(t[i] + h/2, Z1[i] + k1/2, Z2[i] + l1/2, Z3[i] + m1/2, Z4[i] + n1/2)
        n2 = h * f4(t[i] + h/2, Z1[i] + k1/2, Z2[i] + l1/2, Z3[i] + m1/2, Z4[i] + n1/2)

        k3 = h * f1(t[i] + h/2, Z1[i] + k2/2, Z2[i] + l2/2, Z3[i] + m2/2, Z4[i] + n2/2)
        l3 = h * f2(t[i] + h/2, Z1[i] + k2/2, Z2[i] + l2/2, Z3[i] + m2/2, Z4[i] + n2/2)
        m3 = h * f3(t[i] + h/2, Z1[i] + k2/2, Z2[i] + l2/2, Z3[i] + m2/2, Z4[i] + n2/2)
        n3 = h * f4(t[i] + h/2, Z1[i] + k2/2, Z2[i] + l2/2, Z3[i] + m2/2, Z4[i] + n2/2)

        k4 = h * f1(t[i] + h, Z1[i] + k3, Z2[i] + l3, Z3[i] + m3, Z4[i] + n3)
        l4 = h * f2(t[i] + h, Z1[i] + k3, Z2[i] + l3, Z3[i] + m3, Z4[i] + n3)
        m4 = h * f3(t[i] + h, Z1[i] + k3, Z2[i] + l3, Z3[i] + m3, Z4[i] + n3)
        n4 = h * f4(t[i] + h, Z1[i] + k3, Z2[i] + l3, Z3[i] + m3, Z4[i] + n3)

        Z1.append(Z1[i] + (k1 + 2*k2 + 2*k3 + k4) / 6)
        Z2.append(Z2[i] + (l1 + 2*l2 + 2*l3 + l4) / 6)
        Z3.append(Z3[i] + (m1 + 2*m2 + 2*m3 + m4) / 6)
        Z4.append(Z4[i] + (n1 + 2*n2 + 2*n3 + n4) / 6)
        t.append(t[i] + h)

    return Z1, Z3

for b in np.arange(-200.0, 200.0, 10):
    x, y = RK4solver(b)
    plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectories for various impact parameters')
plt.grid(True)
plt.show()
