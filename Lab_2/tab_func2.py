from math import factorial as fac
from math import fabs
import numpy as np

m = 3
n = 1
x = 0
d = 0.001 

ls = np.arange(0.1, 0.5, 0.05)
sigma = []

for x in ls :

    func = ((m *(m + 1)*(m + n - 1))/(fac(n)))*x**n

    if abs(func) >= d :
        sigma.append(func)
        n += 1 


print(1 + sum(sigma))
print(fabs(-1))
