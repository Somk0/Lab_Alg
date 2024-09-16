from math import sin, cos, tan

x = 0.013
z = 1.245

y = sin(x**(cos(z))) + (tan(z))**(sin(x))

y = round(y , 3)

print(y)