from math import factorial as fac

def arange(a ,b ,c):
    r = []

    r.append(a)
    while True:

        if a >= b:
            break

        a = a + c

        r.append(a)
        
    return r 
m = 3
n = 1
x = 0
d = 0.001 

ls = arange(0.1, 0.5, 0.05)

sigma = []

for x in ls :

    func = ((m *(m + 1)*(m + n - 1))/(fac(n)))*x**n

    if func >= d :
        
        sigma.append(func)

    n += 1 

print(1 + sum(sigma))


