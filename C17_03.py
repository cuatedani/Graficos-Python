xi, yi = 1,1
xf,yf = 3,2

x = xi
while x<=xf:
    y = round(yf+-yi)*(x-xi)/(xf-xi) +yi
    print(x, ",", y)
    x += 1
