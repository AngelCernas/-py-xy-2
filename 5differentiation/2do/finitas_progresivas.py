from math import sin

def f(x):
    return ((sin(2*x))**3)/(x**4+1)

x0=2.45
h1=0.8
r1=(f(x0+h1)-f(x0))/h1
print('r1=',r1)

h2=0.5
r2=(f(x0+h2)-f(x0))/h2
print('r2=',r2)

h3=0.1
r3=(f(x0+h3)-f(x0))/h3
print('r3=',r3)

h4=0.00001
r4=(f(x0+h4)-f(x0))/h4
print('r4=',r4)

h5=0.00000001
r5=(f(x0+h5)-f(x0))/h5
print('r5=',r5)

h6=0.0000000001
r6=(f(x0+h6)-f(x0))/h6
print('r6=',r6)