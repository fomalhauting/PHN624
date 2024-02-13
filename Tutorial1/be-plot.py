# if a is even z = A/2    if a is odd z = (a-1)/2
import numpy as np
import matplotlib.pyplot as plt

av = 15.75
as_ = 17.80
ac = 0.71
aa = 23.70
ap = 33.50

arra = np.arange(1, 251)
arrz = np.where(arra%2 == 0, arra//2, (arra-1)//2)

bindingenergy = []
for a,z in zip(arra,arrz):
  BE = av*a - as_*(a**(2/3)) - aa*((a-(2*z))**2)/a - ac*(z**2)/(a**(1/3))
  if a%2 != 0:
    BE = BE
  elif z%2 == 0 and (a-z)%2 == 0:
    BE += ap/(a**(3/4))
  elif z%2 != 0 and (a-z)%2 != 0:
    BE -= ap/(a**(3/4))
  bindingenergy.append(BE/a)

plt.plot(arra, bindingenergy)
plt.show()
