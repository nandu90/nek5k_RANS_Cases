import math
import os
import time
from sympy import *

def main():
    u, cosphi, up, alpha, yplus, utau, beta, C, kappa = symbols('u cosphi up alpha yplus utau beta C kappa')
        
    up_plus = alpha*(log(yplus) + log(up/(utau+up))) + beta
    utau_plus = (1./kappa)*(log(yplus) + log(utau/(utau+up))) + C
    cospsi = (u*cosphi-up*up_plus)/(utau_plus*utau)

    expr = utau**2 + (up*alpha*kappa)**2 + 2*up*alpha*kappa*utau*cospsi
    
    dd_u_tau = diff(expr, utau)

    init_printing()

    pprint(simplify(dd_u_tau))
    return

if __name__ == "__main__":
    starttime = time.time()
    main()
    print("--- Code ran in %s seconds ---"%(time.time()-starttime))
