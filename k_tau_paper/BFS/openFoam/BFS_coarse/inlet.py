from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def main():

    try:
        os.makedirs("constant/boundaryData/inlet/0")
    except FileExistsError:
        pass

    loc="constant/boundaryData/inlet/"
    loc2=loc+'0/'
    data = np.loadtxt('../../wallResolved_omega/InletProf.dat',skiprows=1)
    y = data[:,0]
    u = data[:,1]
    k = data[:,2]
    omg = data[:,3]
    
    #Dirichlet BC Menter
    beta_0 = 0.0708
    alpha = 6
    nu = 1/149700
    yw = 1-np.abs(y)
    omgw = alpha*nu/(beta_0*yw**2.)
    omg = omg+omgw
    
    #Fix boundary
    ylim = 8e-4
    omw = alpha*nu/(beta_0*ylim**2.)
    print(omw,nu)
    omg[0] = omw
    omg[-1] = omw

    y = y+1
    pts = y.size

    #openfoam arrays
    ox = np.ones(pts)*-1
    ox = np.concatenate((ox,ox))
    oy = np.concatenate((y,y))
    oz = np.ones(pts)*0.05
    oz = np.concatenate((oz,np.ones(pts)*-0.05))
    
    #Save coords
    np.savetxt(loc+'points',np.c_[ox,oy,oz],fmt='(%.10e %.10e %.10e)',header=str(pts*2)+'\n(',footer=')',comments='')

    #Save data
    ou = np.concatenate((u,u))
    ovw = np.zeros(pts*2)
    np.savetxt(loc2+'U',np.c_[ou,ovw,ovw],fmt='(%.10e %.10e %.10e)',header=str(pts*2)+'\n(',footer=')',comments='')

    ok = np.concatenate((k,k))
    np.savetxt(loc2+'k',ok,fmt='%.10e',header=str(pts*2)+'\n(',footer=')',comments='')

    oomg = np.concatenate((omg,omg))
    np.savetxt(loc2+'omega',oomg,fmt='%.10e',header=str(pts*2)+'\n(',footer=')',comments='')
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
