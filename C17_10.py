def main():
    xi,yi = 0,0
    xf,yf = 13,15
    
    dx = xf-xi
    dy = yf-yi
    
    xk = xi
    yk = yi
    
    if dx >= dy: 
        while xk <= xf:
            print(xk, yk)
            DPK = 2*xk*dy + 2*yk*dx + 2*yi*dx + 2*xi*dy -dx
            if DPK >= 0:
                yk  += 1
            xk += 1
    else:
        while yk <= yf:
            print(xk,yk)
            DPk = 2*yk*dx + 2*dx - 2*xk*dy + 2*xi*dy - 2*yi*dx - dy
            if DPk >= 0:
                xk += 1
            yk += 1
    
if __name__ == "__main__":
    main()
