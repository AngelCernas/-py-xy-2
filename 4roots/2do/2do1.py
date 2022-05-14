#
# please refer to PPT file
# for exercise
#
from math import exp

def f(x):# Función
    return exp(2-x)-7*x

def f2(x):# Derivada: 
    return -exp(2-x)-7

x0=1.5
x1=x0-f(x0)/f2(x0)

print('x1= ', x1)

x2=x1-f(x1)/f2(x1)
print('x2= ', x2)

x3=x2-f(x2)/f2(x2)
print('x3= ', x3)
print('valor =',f(x3))
print('raiz = ',x3)

'''tl =[-2,-1,0,1,2]
sp =[-61.59,-27.08,-14.38,-9.71,8]

print(plt.scatter(tl,sp))'''
