import math

def main():
    r = 10
  
    xi,xf = 0,r
    x = xi
    while x<=xf:
        y = round(+ math.sqrt(r**2 - x**2))
        print(x,y)
        print(-x,y)
        print(-x,-y)
        print(x,-y)
        x += 1
    print()
    yi,yf = 0,r
    y = yi
    while y<=yf:
        x = round(+ math.sqrt(r**2 - y**2))
        print(x,y)
        print(-x,y)
        print(-x,-y)
        print(x,-y)
        y += 1        
if __name__ == "__main__":
    main()
