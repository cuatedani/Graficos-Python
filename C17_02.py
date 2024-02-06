def f(x):
    m = -2
    b = 1
    return round(m*x+b)

xi = 1
xf = 10

x = xi

while x <= xf:
    y=f(x)
    print(x,",",y)
    x += 1
