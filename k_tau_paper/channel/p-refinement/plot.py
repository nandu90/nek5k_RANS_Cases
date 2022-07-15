from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

nu = 8e-6

def plotnow(fname,tit,xlabel,ylabel,x,y,labels,ptype='line',linestyles=[],markers=[]):
    default_cycler = (cycler(color=['r','k','b','g','k','m'])*\
                      cycler(linestyle=['-'])*cycler(marker=['']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111)  

    ax.set_xlabel(xlabel,fontsize=20)
    ax.set_ylabel(ylabel,fontsize=20)
    ax.tick_params(axis='both',labelsize=15)
    
    # if(len(linestyles) == 0):
    #     linestyles = ['-']*len(x)
    #     markers = ['']*len(x)

    print(linestyles)
    print(len(x))

    for i in range(len(y)):
        if(ptype=='line'):
            ax.plot(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i],linewidth=1.5)
        elif(ptype=='semilogx'):
            ax.semilogx(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i],linewidth=1.5)
        elif(ptype=='semilogy'):
            ax.semilogy(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i])
        else:
            ax.loglog(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i])
    
            
            #plt.title(tit,fontsize=18)
    ax.grid()
    ax.legend(loc='best',fontsize=13)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def getdata(case,fname,x,y,vx,vy,k,tau):
    data = np.loadtxt(case+'/'+fname,skiprows=1)
    x.append(data[:,0])
    y.append(np.flip(data[:,1]))
    
    vx.append(data[:,2])
    vy.append(data[:,3])
    
    k.append(data[:,6])
    tau.append(data[:,7])
    return

def getlocdata(cases,fname,utau):
    x = []
    y = []
    vx = []
    vy = []
    k = []
    tau = []
    yplus = []
    kplus = []
    uplus = []
    tauplus = []
    nut = []
    
    for i in range(len(cases)):
        getdata(cases[i],fname,x,y,vx,vy,k,tau)
        nut.append(k[-1]*tau[-1])
        yplus.append(y[-1]*utau[i]/nu)
        kplus.append(k[-1]/utau[i]**2.)
        uplus.append(vx[-1]/utau[i])
        tauplus.append(tau[-1]*nu/utau[i]**2.)
        tauplus[-1]=tauplus[-1][yplus[-1]>1e-6]
        uplus[-1]=uplus[-1][yplus[-1]>1e-6]
        kplus[-1]=kplus[-1][yplus[-1]>1e-6]
        yplus[-1]=yplus[-1][yplus[-1]>1e-6]
           
    return x,y,vx,vy,k,tau,yplus,kplus,nut,uplus,tauplus

def getexpdata(fname,y,vx,k,yplus,kplus,uplus):
    data = np.loadtxt(fname,delimiter=',',skiprows=1)
    utau = 4.14872e-02
    y.append(data[:,0])
    vx.append(data[:,1]*utau)
    k.append(data[:,2]*utau**2.)
    yplus.append(y[-1]*utau/nu)
    kplus.append(k[-1]/utau**2.)
    uplus.append(vx[-1]/utau)
    uplus[-1]=uplus[-1][yplus[-1]>1e-6]
    kplus[-1]=kplus[-1][yplus[-1]>1e-6]
    yplus[-1]=yplus[-1][yplus[-1]>1e-6]
    return

def getofdata(cases,utau,fname,y,vx,k,yplus,kplus):
    for i in range(len(cases)):
        data = np.loadtxt(cases[i]+'/'+fname,delimiter=',',skiprows=1)
        
        y.append(1-data[:,0])
        vx.append(data[:,1])
        k.append(data[:,4])
        
        yplus.append(y[-1]*math.sqrt(utau[i])/nu)
        kplus.append(k[-1]/math.sqrt(utau[i])**2.)
        kplus[-1]=kplus[-1][yplus[-1]>0.01]
        yplus[-1]=yplus[-1][yplus[-1]>0.01]
    return

def main():
    nekcases = ['p3','p5','p7','p9']
    nekutau = [4.1146E-02,4.1393E-02,4.1189E-02,4.1114E-02]
    
    labels = ['p3','p5','p7','p9','DNS: Lee (2015)']
        
    linestyles = [':',':','--','-','--']
#    linestyles = ['--','-','']
    markers = ['','','','','']
#    markers = ['','','*']

    fname = 'plot.dat'
    x,y,vx,vy,k,tau,yplus,kplus,nut,uplus,tauplus = getlocdata(nekcases,fname,nekutau)
    
    getexpdata('../moser_125k.csv',y,vx,k,yplus,kplus,uplus)
    title = 'U'
    plotnow('U',title,'$y/H$','$u/U$',y,vx,labels,linestyles=linestyles,markers=markers)

    title = 'uplus'
    plotnow('uplus',title,'$y^+$','$U^+$',yplus,uplus,labels,ptype='semilogx',linestyles=linestyles,markers=markers)
    
    title = 'tkeplus'
    plotnow('kplus',title,'$y^+$','$k^+$',yplus,kplus,labels,ptype='semilogx',linestyles=linestyles,markers=markers)

    title = 'TKE'
    plotnow('k',title,'$y/H$','$k/U^2$',yplus,kplus,labels,linestyles=linestyles,markers=markers)

    title = 'tauplus'
    plotnow('tauplus',title,'$y^+$','$\\tau^+$',yplus,tauplus,labels,ptype='semilogx',linestyles=linestyles,markers=markers)

    title = 'nut'
    plotnow('nut',title,'$y/H$','$\\nu_t$',y,nut,labels,ptype='line',linestyles=linestyles,markers=markers)
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
