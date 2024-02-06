xi,yi = 1,1
xf,yf = 1,7

dx = xf-xi
dy = yf-yi

print("dx =",dx,"dy =",dy)

if dx >= dy:
    print("y=f(x)")
    x=xi
    while x <= xf:
        y = round((yf-yi)*(x-xi)/(xf-xi) + yi)
        print(x,",",y)
        x += 1
else:
    print("x = f(y)")
    y = yi
    while y<= yf:
        x = round ((xf-xi)*(y-yi)/(yf-yi) + xi)
        print(x,",",y)
        y += 1
