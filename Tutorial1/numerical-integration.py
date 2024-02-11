# f(x) = x^2 e^(-x^2)    0 <= x <= 2
import numpy as np

def f(x):
  return x**2 * np.exp(-x**2)
  
# midpoint rule
def midpoint_rule(f, a, b, n):
  h = (b - a) / n
  result = 0
  for i in range(n):
    x_mid = a + (i + 0.5) * h
    result += f(x_mid)
  result *= h
  return result

# trapezoidal rule
def trapezoidal_rule(f, a, b, n):
  h = (b - a) / n
  result = 0.5 * (f(a) + f(b))
  for i in range(1, n):
    result += f(a + i * h)
  result *= h
  return result

# simpson's rule
def simpsons_rule(f, a, b, n):
  if n % 2 != 0:
    raise ValueError("Number of intervals must be even for Simpson's rule")
  h = (b - a) / n
  result = f(a) + f(b)
  for i in range(1, n, 2):
    result += 4 * f(a + i * h)
  for i in range(2, n - 1, 2):
    result += 2 * f(a + i * h)
  result *= h / 3
  return result

a = 0
b = 2
n = 1000

midpoint = midpoint_rule(f, a, b, n)
trapezoidal = trapezoidal_rule(f, a, b, n)
simpsons = simpsons_rule(f, a, b, n)

print(midpoint, trapezoidal, simpsons)
