"""Juan Daniel Gomez Gonzalez 
NC:19400588
"""
import math

def main():
    r = 9
    x = 0
    y = r
    DPK = 3 - 2*r
    while x <= y:
        print('DPK: ', DPK)
        print(x,y)
        print(y,x)
        print(x,-y)
        print(y,-x)
        print(-x,y)
        print(-y,x)
        print(-x,-y)
        print(-y,-x)
        
        if DPK >= 0:
            DPK = DPK + 4*(x-y) + 10
            y = y - 1
        else:
            DPK = DPK + 4*x + 6
        x = x + 1
   
if __name__ == "__main__":
    main()
