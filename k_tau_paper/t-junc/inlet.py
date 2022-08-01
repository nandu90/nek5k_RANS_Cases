from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def plotnow(fname,tit,xlabel,ylabel,x,y,labels,ptype='line'):
    default_cycler = (cycler(color=['k','b','r','c','g','m'])*\
                      cycler(linestyle=['-'])*cycler(marker=['']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111)  

    ax.set_xlabel(xlabel,fontsize=20)
    ax.set_ylabel(ylabel,fontsize=20)

    for i in range(len(y)):
        if(ptype=='line'):
            ax.plot(x[i],y[i],label=labels[i])
        elif(ptype=='semilogx'):
            ax.semilogx(x[i],y[i],label=labels[i])
        elif(ptype=='semilogy'):
            ax.semilogy(x[i],y[i],label=labels[i])
        else:
            ax.loglog(x[i],y[i],label=labels[i])
    
            
    plt.title(tit,fontsize=18)
    ax.grid()
    ax.legend(loc='best',fontsize=12)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return


def getdata(fname,x,y,vx,vy,vz,k,tau):
    data = np.loadtxt(fname,skiprows=1)
    x.append(data[:,0])
    y.append(data[:,1])
    vx.append(data[:,3])
    vy.append(data[:,4])
    vz.append(data[:,5])
    k.append(data[:,8])
    tau.append(data[:,9])
    return

def main():
    x = []
    y = []
    vx = []
    vy = []
    vz = []
    k = []
    tau = []
    
    getdata('inlet1/in.00001.dat',x,y,vx,vy,vz,k,tau)
    #getdata('inlet2/in.00001.dat',x,y,vx,vy,vz,k,tau)
    getdata('inlet_kOmega/in.00001.dat',x,y,vx,vy,vz,k,tau)

    r = [y[0]*0.714,y[-1]*0.714]
    U = [vx[0]/0.714,vz[-1]/0.714]
    
    labels = ['x=-5','y=5','omega']
    plotnow('U','U','r','U',r,U,labels)

    s1 = [k[0]/0.714**2.0,k[-1]/0.714**2.0]
    plotnow('k','k','r','k',r,s1,labels)

    #s2 = [tau[0]*0.714**2.,tau[1]]
    #plotnow('tau','tau','r','tau',r,s2,labels)

    #print
    wd = np.abs(y[0]-0.5)
    np.savetxt('InletProf.dat',np.c_[np.flip(wd),np.flip(vx[0]),np.flip(k[0]),np.flip(tau[0])],header='Re40k:r,U,k,tau',delimiter=' ')
    
    #from k-omega
    wd = np.abs(y[-1]-0.5)
    np.savetxt('InletProf_kOmega.dat',np.c_[np.flip(wd),np.flip(vz[-1]),np.flip(k[-1]),np.flip(tau[-1])],header='Re40k:r,U,k,tau',delimiter=' ')
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
