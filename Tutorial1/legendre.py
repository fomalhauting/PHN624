import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-1,1, 0.01)

def legendre(n,x):
  if n == 0:
    return 1
  elif n == 1:
    return x
  else:
    return ((2*n-1)*x*legendre(n-1,x) - (n-1)*legendre(n-2,x))/n

for n in range(6):
    p = [legendre(n, x) for x in X]
    plt.plot(X, p)
  
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()
