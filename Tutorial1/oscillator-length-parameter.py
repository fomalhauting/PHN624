import math

A = 36
hw1 = 41*(A**(-1/3))
hw2 = 45*(A**(-1/3)) - 25*(A**(-2/3))
b1 = 197.33/math.sqrt(940*hw1)
b2 = 197.33/math.sqrt(940*hw2)

print(b1,b2)
print(abs(b1-b2))
