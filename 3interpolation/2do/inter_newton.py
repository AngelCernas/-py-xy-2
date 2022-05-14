p1=(2,1.43)
p2=(3.2,2.79)
p3=(4,3.56)
x=3.6


def fn(x,p1,p2,p3):
    b1=(p2[1]-p1[1])/(p2[0]-p1[0])

    b2=((p3[1]-p2[1])/(p3[0]-p2[0]))

    resultadob=(b2-b1)/(p3[0]-p1[0])

    y=p1[1]+(b1*(x-p1[0]))

    y2=(x-p1[0])*(x-p3[0])

    y3=resultadob*y2
    return  y+y3


print(" x=",x," y=",fn(x,p1,p2,p3))