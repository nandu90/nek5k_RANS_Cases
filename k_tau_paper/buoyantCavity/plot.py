from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plotnow(fname,xlabel,ylabel,x,y,labels,lstyles,mrks,ptype='line'):
    default_cycler = (cycler(color=['k','b','r','c','g','m'])*\
                      cycler(linestyle=['-'])*cycler(marker=['']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    fig = plt.figure(figsize=(7,5))
    
    ax = fig.add_subplot(111)  

    ax.set_xlabel(xlabel,fontsize=15)
    ax.set_ylabel(ylabel,fontsize=15)
    ax.tick_params(axis='both',labelsize=12)

    for i in range(len(y)):
        if(ptype=='line'):
            ax.plot(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i],linewidth = 1.5)
        elif(ptype=='semilogx'):
            ax.semilogx(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i],linewidth=1.5)
        elif(ptype=='semilogy'):
            ax.semilogy(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i])
        else:
            ax.loglog(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i])

    ax.grid()
        
    ax.legend(loc='best',fontsize=12)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def getexpdata(x,v,T,k):
    data = np.loadtxt('exp.csv',delimiter=',')
    x.append(data[:,0])
    v.append(data[:,1])
    T.append(data[:,5])
    k.append(data[:,10])
    return

def getdata(fname,x,v,T,k):
    data = np.loadtxt(fname+'.dat',skiprows=1)
    x.append(data[:,0])
    v.append(data[:,3])
    T.append(data[:,5]+0.5)
    k.append(data[:,6])
    return

def main():
    x=[]
    v=[]
    T=[]
    k=[]
    getexpdata(x,v,T,k)

    cases=['ktau','sgdh','ggdh']
    for c in cases:
        getdata(c,x,v,T,k)
    
    labels = ['Exp','$k-\\tau$','SGDH','GGDH']
    lstyles = ['','-','-','-']
    mrks = ['.','','','']
    plotnow('U','$x/H$','$v/U$',x,v,labels,lstyles,mrks)
    plotnow('T','$x/H$','$(T-T_c)/\Delta T$',x,T,labels,lstyles,mrks)
    plotnow('k','$x/H$','$k/U^2$',x,k,labels,lstyles,mrks)
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
