"""Juan Daniel Gomez Gonzalez 
NC:19400588
"""

def main():
    xi,yi = 0,0
    xf,yf = 10,-3
    
    dx = xf-xi
    dy = yf-yi
    
    xk = xi
    yk = yi
    
    while xk <= xf:
        
        DPK = 2*xk*dy - 2*yk*dx + 2*yi*dx - 2*xi*dy + dx
        print(xk, yk)
        if DPK <= 0:
            yk  -= 1
        xk += 1
        
if __name__ == "__main__":
    main()