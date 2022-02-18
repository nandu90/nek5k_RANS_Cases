from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def plotnow(fname,title,xlabel,ylabel,x,y,labels,ptype='line'):
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

    ax.grid()
    ax.set_title(title,fontsize=15)
    ax.set_ylim([0.0,3.0])
    ax.legend(loc='best',fontsize=12)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def getdata(fname,x,y,vx,vy,p,temp,sc1,sc2):
    data = np.loadtxt(fname,skiprows=1)

    x.append(data[:,0])
    y.append(data[:,1]+1.0)
    vx.append(data[:,2])
    vy.append(data[:,3])
    p.append(data[:,4])
    temp.append(data[:,5])
    sc1.append(data[:,6])
    sc2.append(data[:,7])
    return

def clearDat():
    x = []
    y = []
    vx= []
    vy = []
    p = []
    temp = []
    sc1 = []
    sc2 = []
    return x,y,vx,vy,p,temp,sc1,sc2

def main():
    n = 8
    lbl = "x="
    poslabels = ["-4","0","1.5","2.5","5","6","8","10"]
    
    cases = ['coarse','coarse_2.0','wallResolved']
    labels = ['WF,lx1=4;$\sigma_w=0.5$','WF,lx1=4;$\sigma_w=2.0$','WR,lx1=8']

    for i in range(n):
        x,y,vx,vy,p,temp,sc1,sc2 = clearDat()
        for c in cases:
            fname = c+"/bfs.0000"+str(i+1)+".dat"
            getdata(fname,x,y,vx,vy,p,temp,sc1,sc2)
        title = "x/H="+poslabels[i]
        pname = "Umean_x="+poslabels[i]            
        plotnow(pname,title,"$U/U_{ref}$","$y/H$",vx,y,labels)
        pname = "k_x="+poslabels[i]            
        plotnow(pname,title,"$k/U_{ref}^2$","$y/H$",sc1,y,labels)
        pname = "tau_x="+poslabels[i]            
        plotnow(pname,title,"$\\tau/t$","$y/H$",sc2,y,labels)
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
