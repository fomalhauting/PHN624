import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-10,10,0.1)

def laguerre(n,x):
  if n == 0:
    return 1
  elif n == 1:
    return 1-x
  else:
    return ((2*n-1-x)*laguerre(n-1,x) - (n-1)*laguerre(n-2,x))/n
  
for n in range(6):
  l = [laguerre(n,x) for x in X]
  plt.plot(X,l)

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()
