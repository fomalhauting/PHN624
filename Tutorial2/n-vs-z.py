# N vs Z plots

import numpy as np
import matplotlib.pyplot as plt

av = -16
as_ = 20
ac = 0.751
aa = 21.4
Mn = 1.008665
MH = 1.007825

# Beta stability line
def betastability(A):
    return (ac*np.power(A, 2/3) - (Mn - MH)*931.5) / ((4*aa/A) + ac/np.power(A, 1/3))

# Proton drip-line
def protondrip(A):
    beta = (2*ac*np.power(A, 2/3)) / ((ac*np.power(A, 2/3)) + (12*aa))
    gamma = (av + (3*aa) - ((2/3)*as_*np.power(A, -1/3))) / (((1/3)*ac*np.power(A, 2/3)) + (4*aa))
    discriminant = np.power((1 + beta), 2) - gamma
    #Zplus = A * ((1+beta) + np.sqrt(discriminant))
    Zminus = A * ((1+beta) - np.sqrt(discriminant))
    return Zminus

# Neutron drip-line
def neutrondrip(A):
    alpha = (av + (3*aa) - ((2/3)*as_/np.power(A, 1/3)) + ((ac/3)*np.power(A, 2/3))) / (((ac/3)*np.power(A, 2/3)) + (4*aa))
    discriminant = 1 - alpha
    #Nplus = A * (1 + np.sqrt(discriminant))
    Nminus = A * (1 + np.sqrt(discriminant))
    return  Nminus

A = np.arange(1, 301)
Z = np.arange(1, 301)
Z_betastability = betastability(A)
Z_protondrip_minus = protondrip(A)
N_neutrondrip_plus = neutrondrip(A)

plt.plot(Z, A, label='N = Z', linestyle='dotted')
plt.plot(Z_betastability, A, label='Beta Stability Line', linestyle='--')
plt.plot(Z_protondrip_minus, A, label='Proton Drip Line', linestyle='-')
plt.plot(N_neutrondrip_plus, A, label='Neutron Drip Line', linestyle='-.')
plt.title('N vs. Z for Nuclear Stability Lines')
plt.xlabel('Z')
plt.ylabel('N')
plt.legend()
plt.grid(True)
plt.show()

# N vs Z plots
'''
import numpy as np
import matplotlib.pyplot as plt

# Constants
a_v = 15.8
a_s = 18.3
a_c = 0.714
a_sym = 21.4
Mn = 1.008665
MH = 1.007825
# Function definitions
def beta_stability(A):
    N = (A + (a_c * A ** (2/3) - (Mn - MH)*931.5)/(4 * a_sym / A + a_c/(A**(1/3))))/2
    Z = A - N
    return int(N), int(Z)

def proton_drip_line(A):
    beta = (2 * a_c * A ** (2/3)) /  (a_c * A ** (2/3) + 12 * a_sym)
    gamma = (a_v + 3 * a_sym - (2/3) * a_s * A ** (-1/3)) / ((1 / 3) * a_c * A ** (2/3) + 4 * a_sym)
    Z = A * ((1 + beta) - np.sqrt((1 + beta)**2 - gamma))
    N = A - Z
    return int(N), int(Z)

def neutron_drip_line(A):
    alpha = (a_v + 3 * a_sym - (2/3) * a_s / A**(1/3) + a_c * A**(2/3)/3) / (a_c * A**(2/3)/3 + 4 * a_sym)
    N = A * (1 - np.sqrt(1 - alpha))
    Z = A - N
    return int(N), int(Z)

# Data generation
beta_N, beta_Z = zip(*[beta_stability(i) for i in range(1, 150)])
proton_N, proton_Z = zip(*[proton_drip_line(i) for i in range(1, 150)])
neutron_N, neutron_Z = zip(*[neutron_drip_line(i) for i in range(1, 150)])

# Plotting
plt.figure(figsize=(8, 6))
plt.title("N-Z Chart for Nuclear Stability", fontsize=16)
plt.xlabel("N (Neutrons)", fontsize=12)
plt.ylabel("Z (Protons)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.plot(beta_N, beta_Z, label="Beta Stability Line")
plt.plot(proton_N, proton_Z, label="Proton Drip Line")
plt.plot(neutron_N, neutron_Z, label="Neutron Drip Line")
plt.plot(np.arange(1, 150), np.arange(1, 150), linestyle='dashed', label="N = Z Line")
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
'''
