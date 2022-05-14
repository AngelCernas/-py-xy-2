#
# radious of circle inscribed in a triangle
# place here your solution code
#
# zeeAlso
# https://keisan.casio.com/exec/system/1223428152

import math as m
a=None
b=None
c=None

while True:
    try:
        a=float(input('Esribe el primer lado del triangulo'))
        break
    except:
        print('Debes escribir un numero.')

while True:
    try:
        b=float(input('Esribe el segundo lado del triangulo'))
        break
    except:
        print('Debes escribir un numero.')

while True:
    try:
        c=float(input('Esribe el tercer lado del triangulo'))
        break
    except:
        print('Debes escribir un numero.')


s = (a+b+c)*(1/2)

print(s)

r = m.sqrt(s*((s-a)*(s-b)*(s-c))/s)
print(r)
