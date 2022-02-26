from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def plotnow(fname,title,xlabel,ylabel,x,y,labels,lstyles,mrks,ptype='line'):
    default_cycler = (cycler(color=['k','b','r','c','g','m'])*\
                      cycler(linestyle=['-'])*cycler(marker=['']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    fig = plt.figure(figsize=(3,5))
    ax = fig.add_subplot(111)  

    ax.set_xlabel(xlabel,fontsize=15)
    ax.set_ylabel(ylabel,fontsize=15)

    for i in range(len(y)):
        if(ptype=='line'):
            ax.plot(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i])
        elif(ptype=='semilogx'):
            ax.semilogx(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i])
        elif(ptype=='semilogy'):
            ax.semilogy(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i])
        else:
            ax.loglog(x[i],y[i],label=labels[i],linestyle=lstyles[i],marker=mrks[i])

    ax.grid()
    ax.set_title(title,fontsize=15)
    ax.set_ylim([0.0,3.0])
    ax.legend(loc='best',fontsize=10)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def getdata(fname,x,y,vx,vy,p,temp,sc1,sc2,uref):
    data = np.loadtxt(fname,skiprows=1)

    x.append(data[:,0])
    y.append(data[:,1]+1.0)
    vx.append(data[:,2]/uref)
    vy.append(data[:,3])
    p.append(data[:,4])
    temp.append(data[:,5])
    sc1.append(data[:,6]/uref**2.0)
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

def getExpData(index):
    i = 1+index
    data = np.loadtxt("expData/u"+str(i)+".dat",delimiter=",")
    u = data[:,0]
    yu = data[:,1]
    data = np.loadtxt("expData/k"+str(i)+".dat",delimiter=",")
    k  =data[:,0]
    yk = data[:,1]
    return u,yu,k,yk

def main():
    
    n = 8
    lbl = "x="
    poslabels = ["-4","0","1.5","2.5","5","6","8","10"]
    
    cases = ['coarse_2.0','coarse_WF','coarse_spline','wallResolved','wallResolved_spline']
    cases = ['wallResolved','coarse_2.0','coarse_WF']
#    cases = ['wallResolved_spline','coarse_spline']

    labels = ['WR_inlet','WF_inlet','SPLINE','WR,lx1=8','WR,lx1=8_spline']
    labels = ['WR','WF_WR-inlet','WF_WF-inlet']
#    labels = ['WR','WF']
    
    lstyles = ['','--','-','-']
    mrks = ['.','','','']
#    lstyles = ['','--','-']
#    mrks = ['.','','']

    uref1 = 1.0#7392
    uref = [uref1,uref1,1.0,uref1,1.0]
    uref = [uref1,uref1,uref1]
#    uref = [1.0,1.0]

    for i in range(n):
        uexp,yuexp,kexp,kyexp = getExpData(i)
        x,y,vx,vy,p,temp,sc1,sc2 = clearDat()
        for c in range(len(cases)):
            fname = cases[c]+"/bfs.0000"+str(i+1)+".dat"
            getdata(fname,x,y,vx,vy,p,temp,sc1,sc2,uref[c])
        title = "x/H="+poslabels[i]

        pname = "Umean_x="+poslabels[i]            
        xdata = vx.copy()
        xdata.insert(0,uexp)
        ydata = y.copy()
        ydata.insert(0,yuexp)
        lbs = labels.copy()
        lbs.insert(0,'Exp')
        plotnow(pname,title,"$U/U_{ref}$","$y/H$",xdata,ydata,lbs,lstyles,mrks)

        pname = "k_x="+poslabels[i]            
        xdata = sc1.copy()
        xdata.insert(0,kexp)
        ydata = y.copy()
        ydata.insert(0,kyexp)
        lbs = labels.copy()
        lbs.insert(0,'Exp')
        print(len(xdata),len(ydata),len(lbs))
        plotnow(pname,title,"$k/U_{ref}^2$","$y/H$",xdata,ydata,lbs,lstyles,mrks)

        pname = "tau_x="+poslabels[i]            
        plotnow(pname,title,"$\\tau/t$","$y/H$",sc2,y,labels,lstyles,mrks)
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
