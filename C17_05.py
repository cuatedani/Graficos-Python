import math

xi,xf = -10,10

x=xi
while x <= xf:
    y = x**2 -2
    print(x,",",y)
    x += 1


yi,yf = -10,10

x=xi
while x <= xf:
    x = round (math.sqrt(y+2))
    print(x,",",y)
    y += 1
