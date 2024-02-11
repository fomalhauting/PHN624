import numpy as np
import matplotlib.pyplot as plt

def doublefactorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * doublefactorial(n - 2);

X = np.arange(-1, 1, 0.01)

def legendre(n,x):
  if n == 0:
    return 1
  elif n == 1:
    return x
  else:
    return ((2*n-1)*x*legendre(n-1,x) - (n-1)*legendre(n-2,x))/n

plt.figure(figsize=(8, 6))
for n in range(6):
    p = [legendre(n, x) for x in X]
    plt.plot(X, p)

def associated(l, m, x):
    if l == 0:
        return 1
    elif l == 1:
        if m == 0:
            return x
        elif m == 1:
            return -np.sqrt(1 - x**2)
    else:
        if m < 0:
          return (-1**abs(m))*(np.math.factorial(l-abs(m))/np.math.factorial(l+abs(m)))*associated(l, abs(m), x)
        elif m == l:
          return (-1**l)*doublefactorial(2*l-1)*((1-(x**2))**l/2)
        elif m == l-1:
          return x*(2*l+1)*associated(l, l, x)
        else:
          return (x*(2*l-1)*associated(l-1,m,x) - (l+m-1)*associated(l-2, m, x))/(l-m)

plt.figure(figsize=(8, 6))
for l in range(6):
    for m in range(l+1):
        P = [associated(l, m, x) for x in X]
        plt.plot(X, P)

plt.xlim(-2,2)
plt.ylim(-2,2)
