def main():
    xi,yi = 0,0
    xf,yf = 15,0
    
    dx,dy =xf-xi,yf-yi
    
    xk,yk = xi,yi
    
    while xk <=xf:
        print(xk, yk)
        DPK = 2*xk*dy + 2*yk*dx + 2*yi*dx + 2*xi*dy -dx
        if DPK >= 0:
            yk  += 1
        xk += 1
        
if __name__ == "__main__":
    main()