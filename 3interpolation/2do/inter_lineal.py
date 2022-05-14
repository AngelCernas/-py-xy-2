
#interpolacion lineal
p1=(-4,-2)
p2=(1,5)
#estimacion de valor de y 
y=3.7

def fn(y,p1,p2):
    a=(y-p1[1])*(p2[0]-p1[0])
    b=(p2[1]-p1[1])
    return p1[0]+(a/b)

print("cunado se estima Y=",y," X=",fn(y,p1,p2))