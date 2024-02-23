# transmission probability

import numpy as np
import math as mt

# Defining all constants
E = 8.0e-13  # Joules
Z = 92
A = 238
q = 1.6e-19
m = 6.6446e-27  # Kg
hbar = 1.05457182e-34  # kg/s
c1 = 2 * m / (hbar ** 2)
k = 9.0e9  # Coulomb potential constant

def integrand(r):
    V = k * 2 * Z * (q ** 2) / r
    func = (c1 * (abs(V - E))) ** 0.5
    return func

def composite_simpson_integrator(f, number_of_interval=200):
    # Lower limit
    r1 = 1.07 * (A ** (1 / 3)) * (10 ** (-15))
    # Upper limit
    r2 = 8.0 * (A ** (1 / 3)) * (10 ** (-15))

    h = (r2 - r1) / number_of_interval

    x = np.arange(r1, r2 + h, h)

    sum = integrand(x[0]) + integrand(x[-1])

    for i in range(1, number_of_interval):
        if i % 2 == 0:
            sum += 2 * integrand(x[i])
        else:
            sum += 4 * integrand(x[i])

    return h * sum / 3

T = np.exp(-2 * composite_simpson_integrator(integrand))

# To find half-life
f = (2 * E / m) ** 0.5
lambdda = T * f
half_life = mt.log(2) / lambdda
half_life
