from math import sin, cos, fabs, log, e
import numpy as np

ls = np.arange(7.5, 10, 0.2)


i = 1
x = 0


for x in ls:
    func_1 = ((x**2) - 1)**(x - 1)
    func_2 = 1 / (sin(x) + fabs(cos(x)))
    func_3 = log((e**x) + 4)

    if x <= 8 :
        print("1. "f"{i} : {func_1}")
        i = i + 1
    elif 8 < x and x <= 9 :
        print("2. "f"{i} : {func_2}")
        i = i + 1
    elif x > 9 :
        print("3. "f"{i} : {func_3}")
        i = i + 1


print('Done')