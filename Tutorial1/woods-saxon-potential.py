import numpy as np
import matplotlib.pyplot as plt

a = 0.5
R = 5
v0 = -25

x = []
vr = []
for r in np.arange(-10,11,1):
  x.append(r)
  vr.append(v0/(1+np.exp((abs(r)-R)/a)))

plt.plot(x,vr)
plt.show()
