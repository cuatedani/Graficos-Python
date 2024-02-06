xi,yi = -3,2
xf,yf = 5,1

dx = xf-xi
dy = yf-yi

print("dx =",dx,"dy = ",dy)

if abs(dx) >= abs(dy):
        print("y = f(x)")
        x = xi
        if dx<0:
            while x >= xf:
                y = round((yf-yi)*(x-xi)/(xf-xi) + yi)
                print(x,",",y)
                x += -1
        else:
            while x <= xf:
                y = round((yf-yi)*(x-xi)/(xf-xi) + yi)
                print(x,",",y)
                x += 1
else:
        print("x = f(y)")
        y = yi
        if dy<0:
            while y >= yf:
                 x = round((xf-xi)*(y-yi)/(yf-yi) + xi)
                 print(x,",",y)
                 y += -1
        else:
            while y <= yf:
                 x = round((xf-xi)*(y-yi)/(yf-yi) + xi)
                 print(x,",",y)
                 y += 1
