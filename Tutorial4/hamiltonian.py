## hamiltonian eigen values


import numpy as np
import matplotlib.pyplot as plt

MeV, fm, c, ω, m, ℏ = 1, 1, 1, 1, 1, 1
C = -0.15 * ℏ * ω
D = -0.0225 * ℏ * ω
X = [-0.5, 0, 0.5, 1]
N = 4
L = {0: "s", 1: "p", 2: "d", 3: "f", 4: "g"}
E_dict = {}

def energizer(n, l, j):
    ls = l / 2 if l == j - 0.5 else -1 * (l + 1) / 2
    l_2 = l * (l + 1)
    E0 = (n + 1.5) * ℏ * ω
    E = []
    for x in X:
        if x <= 0: E.append(E0)
        else: E.append(E0 + C * ls + D * l_2)
    return E

plt.figure(figsize=(5, 15))
for n in range(N+1):
    E_dict[n] = {}
    for l in range(n, -1, -2):
        if not l:
            j = 0.5
            E = energizer(n, l, j)
            plt.plot(X, E)
            E_dict[n][f"{L[l]}({int(j*2)}/2)"] = f"{E[-1]:.3f}"
        else:
            J = [l - 0.5, l + 0.5]
            for j in J:
                E = energizer(n, l, j)
                plt.plot(X, E)
                E_dict[n][f"{L[l]}({int(j*2)}/2)"] = f"{E[-1]:.3f}"

plt.show()
