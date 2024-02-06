"""Juan Daniel Gomez Gonzalez 
NC:19400588
Algoritmo DDA"""

x1,y1 = 0,0
x2,y2 = -3,10

dx = x2-x1
dy = y2-y1


if abs(dx) >= abs(dy):
    pasos = abs(dx)
else:
    pasos = abs(dy)

print (pasos)
ix = dx/pasos
iy = dy/pasos

x = x1
y = y1
i = 0

while i <= pasos:
    print("Paso #",i,": X = ",round(x)," - Y = ",round(y))
    x= x + ix
    y = y + iy
    i = i + 1