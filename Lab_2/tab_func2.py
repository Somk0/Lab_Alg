from math import factorial as fak
import numpy as np

m = 3
n = 1
x = 0

ls = np.arange(0.1, 0.5, 0.05)
sigma = []

for x in ls :

    func = ((m *(m + 1)*(m + n - 1))/(fak(n)))*x**n
    
    if x <= ls[-1] :
        sigma.append(func)
        n += 1  


print(1 + sum(sigma))
