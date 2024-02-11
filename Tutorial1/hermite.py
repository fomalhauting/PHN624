# H(n) = 2*x*H(n-1) - 2*(n-1)*H(n-2)
# H0(x) = 1    H1(x) = 2*x
import numpy as np
import matplotlib.pyplot as plt

def hermite(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2*x*hermite(x,n-1) - 2*(n-1)*hermite(x,n-2)

X = np.arange(-4, 4.1,0.1)

for n in range(7):
  H = [hermite(x, n) for x in X]
  plt.plot(X, H)

plt.xlim(-4, 4)
plt.ylim(-10,10)
plt.show()

'''
H0 = []
for x in np.arange(-4,4.1,0.1):
  H0.append(hermite(x,0))
print(H0)

H1 = []
for x in np.arange(-4,4.1,0.1):
  H1.append(hermite(x,1))
print(H1)

plt.plot(X,H0)
plt.plot(X,H1)
'''
