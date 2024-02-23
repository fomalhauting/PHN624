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
