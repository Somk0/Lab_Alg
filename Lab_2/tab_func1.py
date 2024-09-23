from math import sin, cos, fabs, log, e
import numpy as np

ls = np.arange(7.5, 10, 0.2)


i = 1
x = 0
range_1 = 8
range_2 = 9


for x in ls:
    func_1 = ((x**2) - 1)**(x - 1)
    func_2 = 1 / (sin(x) + fabs(cos(x)))
    func_3 = log((e**x) + 4)

    if x <= range_1 :
        print("1. "f"{i} : {func_1}")
        i = i + 1
    elif range_1 < x and x <= range_2 :
        print("2. "f"{i} : {func_2}")
        i = i + 1
    elif x > range_2 :
        print("3. "f"{i} : {func_3}")
        i = i + 1


print('Done')