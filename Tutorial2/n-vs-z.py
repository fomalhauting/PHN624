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
    return (ac*np.power(A, 2/3) - (Mn-MH)*931.5) / ((4*aa/A) + ac/np.power(A, 1/3))

# Proton drip-line
def protondrip(A):
    beta = (2*ac*np.power(A, 2/3)) / ((ac*np.power(A, 2/3)) + (12*aa))
    gamma = (av + (3*aa) - ((2/3)*as_*np.power(A, -1/3))) / (((1/3)*ac*np.power(A, 2/3)) + (4*aa))
    discriminant = np.power((1 + beta), 2) - gamma
    Zplus = A * ((1+beta)+np.sqrt(discriminant))
    Zminus = A * ((1+beta)-np.sqrt(discriminant))
    return Zplus, Zminus

# Neutron drip-line
def neutrondrip(A):
    alpha = (av + (3*aa) - ((2/3)*as_/np.power(A, 1/3)) + ((ac/3)*np.power(A, 2/3))) / (((ac/3)*np.power(A, 2/3)) + (4*aa))
    discriminant = 1 - alpha
    Nplus = A * (1+np.sqrt(discriminant))
    Nminus = A * (1-np.sqrt(discriminant))
    return Nplus, Nminus

A = np.arange(1, 300)
Z_betastability = betastability(A)
Z_protondrip_plus, Z_protondrip_minus = protondrip(A)
N_neutrondrip_plus, N_neutrondrip_minus = neutrondrip(A)

plt.plot(Z_betastability, A, label='Beta Stability Line', linestyle='--')
plt.title('N vs. Z for Beta Stability Line')
plt.show()

# Proton drip-line
plt.plot(Z_protondrip_plus, A, label='Proton Drip Line (+)', linestyle='-')
plt.plot(Z_protondrip_minus, A, label='Proton Drip Line (-)', linestyle='-')
plt.title('N vs. Z for Proton Drip Line')
plt.show()

# Neutron drip-line
plt.plot(N_neutrondrip_plus, A, label='Neutron Drip Line (+)', linestyle='-.')
plt.plot(N_neutrondrip_minus, A, label='Neutron Drip Line (-)', linestyle='-.')
plt.title('N vs. Z for Neutron Drip Line')
plt.show()
