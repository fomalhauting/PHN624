# hydrogen atom

import numpy as np
import matplotlib.pyplot as plt

def f(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def df(n):
    result = 1
    for i in range(2, n + 1, 2):
        result *= i
    return result

def Lnk(x, n, k):
    if n == 0: return np.array([1.0 for _ in x])
    if n == 1: return 1 + k - x
    return ((2 * n - 1 + k - x) * Lnk(x, n - 1, k) - (n - 1 + k) * Lnk(x,n-2,k))/n

def Plm(x,l,m):
    if l < abs(m): return x - x
    if m < 0: return (-1) ** abs(m) * f(l - abs(m)) / f(l + abs(m)) * Plm(x, l, abs(m))
    if l == m: return (-1) ** l * df(2 * l - 1) * (1 - x ** 2) ** (l / 2)
    if l == m+1: return x * (2 * m + 1) * Plm(x, m, m)
    return (x * (2 * l - 1) * Plm(x, l-1, m) - (l + m - 1) * Plm(x, l-2, m)) / (l - m)
    

def Ylm(l, m, t, p):
    return (-1) ** m * np.sqrt((2 * l + 1) / (4 * np.pi) * f(l - m) / f(l + m)) * Plm(np.cos(t), l, m) * np.exp(1j*m*p)

def Rnl(r, n, l):
    R = np.sqrt((2 / n) ** 3 * f(n - l - 1) / (2 * n * f(n + l) ** 3))
    return R * np.exp(-r / n) * (2 * r / n) ** l * Lnk(2 * r / n, n - l - 1, 2 * l + 1)

def psinlm(r, n, l, m, t, p):
    return Rnl(r, n, l) * Ylm(l, m, t, p)

fig = plt.figure(figsize=(10, 10))

n, l = 3, 2
r, t, p = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, np.pi, 100), np.linspace(0, 3 * np.pi / 2, 100))

proj = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])

c = 0
for m in range(-l, l + 1):
    c += 1
    
    Ψ = np.abs(psinlm(r, n, l, m, t, p))
    
    Ψx, Ψy, Ψz = Ψ ** 2 * proj
    
    ax = fig.add_subplot(2, 3, c, projection='3d')
    plt.title(f"n={n}, l={l}, m={m}")
    
    ax.scatter(Ψx, Ψy, Ψz, c = Ψ, cmap="plasma")

plt.show()

r = np.arange(0, 30, 0.1)

fig = plt.figure(figsize=(10, 10))

c = 0
for n in range(1, 4):
    for l in range(n):
        c += 1
        fig.add_subplot(4, 2, c)
        plt.title(f"n={n}, l={l}")
        plt.plot(r, Rnl(r, n, l))

plt.tight_layout()
plt.show()



fig = plt.figure(figsize=(10, 10))

n = 3
r, t, p = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, np.pi, 100), np.linspace(0, 3 * np.pi / 2, 100))

proj = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])

c = 0
for l in range(3):
    for m in range(-l, l + 1):
        c += 1
        
        Ψ = np.abs(psinlm(r, n, l, m, t, p))
        
        Ψx, Ψy, Ψz = Ψ ** 2 * proj
        
        ax = fig.add_subplot(3, 3, c, projection='3d')
        plt.title(f"n={n}, l={l}, m={m}")
        
        ax.scatter(Ψx, Ψy, Ψz, c = Ψ, cmap="viridis")

plt.show()


'''
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def df(n):
    result = 1
    for i in range(2, n + 1, 2):
        result *= i
    return result

def Lnk(x, n, k):
    if n == 0: return np.array([1.0 for _ in x])
    if n == 1: return 1 + k - x
    return ((2 * n - 1 + k - x) * Lnk(x, n - 1, k) - (n - 1 + k) * Lnk(x,n-2,k))/n

def Plm(x,l,m):
    if l < abs(m): return x - x
    if m < 0: return (-1) ** abs(m) * f(l - abs(m)) / f(l + abs(m)) * Plm(x, l, abs(m))
    if l == m: return (-1) ** l * df(2 * l - 1) * (1 - x ** 2) ** (l / 2)
    if l == m+1: return x * (2 * m + 1) * Plm(x, m, m)
    return (x * (2 * l - 1) * Plm(x, l-1, m) - (l + m - 1) * Plm(x, l-2, m)) / (l - m)
    

def Ylm(l, m, t, p):
    return (-1) ** m * np.sqrt((2 * l + 1) / (4 * np.pi) * f(l - m) / f(l + m)) * Plm(np.cos(t), l, m) * np.exp(1j*m*p)

def Rnl(r, n, l):
    R = np.sqrt((2 / n) ** 3 * f(n - l - 1) / (2 * n * f(n + l) ** 3))
    return R * np.exp(-r / n) * (2 * r / n) ** l * Lnk(2 * r / n, n - l - 1, 2 * l + 1)

def psinlm(r, n, l, m, t, p):
    return Rnl(r, n, l) * Ylm(l, m, t, p)

# Set the values of n, l, and m for plotting
n = 2
l = 0
m = 0

fig = plt.figure(figsize=(10, 10))

r, t, p = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 100))

proj = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])

c = 0
for m_value in [m]:
    c += 1
    
    Ψ = np.abs(psinlm(r, n, l, m_value, t, p))
    
    Ψx, Ψy, Ψz = Ψ ** 2 * proj
    
    ax = fig.add_subplot(1, 1, c, projection='3d')
    plt.title(f"n={n}, l={l}, m={m_value}")
    
    ax.scatter(Ψx, Ψy, Ψz, c = Ψ, cmap="plasma")

plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def df(n):
    result = 1
    for i in range(2, n + 1, 2):
        result *= i
    return result

def Lnk(x, n, k):
    if n == 0: return np.array([1.0 for _ in x])
    if n == 1: return 1 + k - x
    return ((2 * n - 1 + k - x) * Lnk(x, n - 1, k) - (n - 1 + k) * Lnk(x,n-2,k))/n

def Plm(x,l,m):
    if l < abs(m): return x - x
    if m < 0: return (-1) ** abs(m) * f(l - abs(m)) / f(l + abs(m)) * Plm(x, l, abs(m))
    if l == m: return (-1) ** l * df(2 * l - 1) * (1 - x ** 2) ** (l / 2)
    if l == m+1: return x * (2 * m + 1) * Plm(x, m, m)
    return (x * (2 * l - 1) * Plm(x, l-1, m) - (l + m - 1) * Plm(x, l-2, m)) / (l - m)
    

def Ylm(l, m, t, p):
    return (-1) ** m * np.sqrt((2 * l + 1) / (4 * np.pi) * f(l - m) / f(l + m)) * Plm(np.cos(t), l, m) * np.exp(1j*m*p)

def Rnl(r, n, l):
    R = np.sqrt((2 / n) ** 3 * f(n - l - 1) / (2 * n * f(n + l) ** 3))
    return R * np.exp(-r / n) * (2 * r / n) ** l * Lnk(2 * r / n, n - l - 1, 2 * l + 1)

def psinlm(r, n, l, m, t, p):
    return Rnl(r, n, l) * Ylm(l, m, t, p)

# Set the values of n, l, and m for plotting
n = 2
l = 0
m = 0

fig = plt.figure(figsize=(10, 10))

r, t, p = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, np.pi, 100), np.linspace(0, 3 * np.pi / 2, 100))

proj = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])

c = 0
for m_value in [m]:
    c += 1
    
    Ψ = np.abs(psinlm(r, n, l, m_value, t, p))
    
    Ψx, Ψy, Ψz = Ψ ** 2 * proj
    
    ax = fig.add_subplot(1, 1, c, projection='3d')
    plt.title(f"n={n}, l={l}, m={m_value}")
    
    ax.scatter(Ψx, Ψy, Ψz, c = Ψ, cmap="plasma")

plt.show()

'''
