## schrodinger finite eigen

import matplotlib.pyplot as plt
import numpy as np

# CONSTANTS

# MeV, fm, c = 1.60218e-13, 1e-15, 3e8
MeV, fm, c = 1, 1, 1
m = 938.272 * MeV / c ** 2
ℏ = 197.3269631 * MeV * fm / c

# Es = [0.51301 * MeV, 2.04 * MeV, 4.6 * MeV]

def schrödinger_finite(n, E):
    V0 = 25 * MeV
    # At x = -L
    x = -12 * fm
    xn = 12 * fm
    z1 = 0
    z2 = 0.0001
    Z1, X = [z1], [x]
    h = (xn - x) / n

    def f1(x, z1, z2):
        return z2

    def f2(x, z1, z2):
        V = V0 if (x <= -10 * fm or x >= 10 * fm) else 0
        return 2 * m / ℏ ** 2 * (V - E) * z1

    for _ in range(n):

        k11 = h * f1(x, z1, z2)
        k12 = h * f2(x, z1, z2)

        k21 = h * f1(x + h/2, z1 + k11/2, z2 + k12/2)
        k22 = h * f2(x + h/2, z1 + k11/2, z2 + k12/2)

        k31 = h * f1(x + h/2, z1 + k21/2, z2 + k22/2)
        k32 = h * f2(x + h/2, z1 + k21/2, z2 + k22/2)

        k41 = h * f1(x + h, z1 + k31, z2 + k32)
        k42 = h * f2(x + h, z1 + k31, z2 + k32)

        x = x + h
        z1 = z1 + (k11 + 2 * (k21 + k31) + k41) / 6
        z2 = z2 + (k12 + 2 * (k22 + k32) + k42) / 6

        X.append(x)
        Z1.append(z1)

    return X, Z1

E = 0.001 * MeV
while E < 20 * MeV:
    X, Ψ = schrödinger_finite(100, E)
    if Ψ[-1] * Ψ[-2] < 0:
        nodes = 0
        for i in range(1, len(Ψ)):
            if Ψ[i] * Ψ[i-1] < 0: nodes += 1
        E_ = np.round(E/MeV, 4)
        print(f"n = {nodes} --> E = {E_}")
        plt.plot(X, Ψ, label=f"{E_}")
        E += 1 * MeV
    E += 0.001 * MeV

plt.scatter([-10 for _ in range(100)], np.linspace(-0.002, 0.003, 100), s = 0.5)
plt.scatter([10 for _ in range(100)], np.linspace(-0.002, 0.003, 100), s = 0.5)

plt.legend()
plt.show()
