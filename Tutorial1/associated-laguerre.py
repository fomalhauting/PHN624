import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-15,15,0.1)

def associatedlaguerre(n, k, x):
  ans = 0
  for m in range(n+1):
    ans += (-1**m)*(np.math.factorial(n+k)/(np.math.factorial(n-m)*np.math.factorial(k+m)*np.math.factorial(m)))*(x**m)
  return ans

for n in range(6):
  for k in range(n+1):
    L = [associatedlaguerre(n,k,x) for x in X]
    plt.plot(X,L)

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()
