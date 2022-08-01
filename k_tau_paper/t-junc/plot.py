from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def plotnow(fname,tit,xlabel,ylabel,x,y,labels,ptype='line',linestyles=[],markers=[]):
    default_cycler = (cycler(color=['k','b','r','c','g','m'])*\
                      cycler(linestyle=['-'])*cycler(marker=['']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111)  

    ax.set_xlabel(xlabel,fontsize=15)
    ax.set_ylabel(ylabel,fontsize=15)
    ax.tick_params(axis='both',labelsize=12)

    # if(len(linestyles) == 0):
    #     linestyles = ['-']*len(x)
    #     markers = ['']*len(x)

    print(linestyles)
    print(len(x))

    for i in range(len(y)):
        if(ptype=='line'):
            ax.plot(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i],linewidth=1.5)
        elif(ptype=='semilogx'):
            ax.semilogx(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i])
        elif(ptype=='semilogy'):
            ax.semilogy(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i])
        else:
            ax.loglog(x[i],y[i],label=labels[i],linestyle=linestyles[i],marker=markers[i])
    
            
#    plt.title(tit,fontsize=18)
    ax.grid()
    ax.legend(loc='best',fontsize=12)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def getdata(case,fname,x,y,z,vx,vy,vz,k,tau):
    data = np.loadtxt(case+'/'+fname,skiprows=1)
    x.append(data[:,0])
    y.append(data[:,1])
    z.append(data[:,2])
    vx.append(data[:,3])
    vy.append(data[:,4])
    vz.append(data[:,5])
    k.append(data[:,8])
    tau.append(data[:,9])
    return

def getlocdata(cases,fname):
    x = []
    y = []
    z = []
    vx = []
    vy = []
    vz = []
    k = []
    tau = []
    
    for i in range(len(cases)):
        getdata(cases[i],fname,x,y,z,vx,vy,vz,k,tau)
   
    return x,y,z,vx,vy,vz,k,tau

def getexpData(fname,x,y):
    data = np.loadtxt('expData/'+fname+".csv",delimiter=',')

    x.insert(0,data[:,0])
    y.insert(0,data[:,1])
    
    return

def main():
    
    cases = ['coarse/tplots','coarse_newton/tplots','coarse_ut1/tplots','coarse_max','wallResolved/tplots','wallResolved_kOmega/tplots']
    cases = ['wallResolved','wallResolved/tplots','wallResolved_kOmega','wallResolved_kOmega/tplots']
    cases = ['wallResolved/tplots','wallResolved_kOmega/tplots']
    labels = ['WF,$k-\\tau$','WF-Newt, $k-\\tau$','WF-$u_\\tau^1$, $k-\\tau$','WF-GM, $k-\\tau$','WR, $k-\\tau$','WR, $k-\omega$ (reg)']
    labels = ['$k-\\tau$','$k-\\omega$(reg)']

    labels.insert(0,'Exp.')
    linestyles = ['--','--','--','--','-','-','']
    linestyles = ['','-','--','--','']
    markers = ['','','','','','','*']
    markers = ['.','','']

    fname = 'tjunc.00001.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x1.6h'
    getexpData('1.6h',z,vx)
    title = 'x=1.6, horizontal'
    plotnow(pname,title,'$z/D$','$u/U_{ref}$',z,vx,labels,linestyles=linestyles,markers=markers)
    
    fname = 'tjunc.00002.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x1.6v'
    getexpData('1.6v',y,vx)
    title = 'x=1.6, vertical'
    plotnow(pname,title,'$y/D$','$u/U_{ref}$',y,vx,labels,linestyles=linestyles,markers=markers)

    fname = 'tjunc.00003.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x2.6h'
    getexpData('2.6h',z,vx)
    title = 'x=2.6, horizontal'
    plotnow(pname,title,'$z/D$','$u/U_{ref}$',z,vx,labels,linestyles=linestyles,markers=markers)

    fname = 'tjunc.00004.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x2.6v'
    getexpData('2.6v',y,vx)
    title = 'x=2.6, vertical'
    plotnow(pname,title,'$y/D$','$u/U_{ref}$',y,vx,labels,linestyles=linestyles,markers=markers)

    fname = 'tjunc.00005.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x3.6h'
    getexpData('3.6h',z,vx)
    title = 'x=3.6, horizontal'
    plotnow(pname,title,'$z/D$','$u/U_{ref}$',z,vx,labels,linestyles=linestyles,markers=markers)

    fname = 'tjunc.00006.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x3.6v'
    getexpData('3.6v',y,vx)
    title = 'x=3.6, vertical'
    plotnow(pname,title,'$y/D$','$u/U_{ref}$',y,vx,labels,linestyles=linestyles,markers=markers)

    fname = 'tjunc.00007.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x4.6h'
    getexpData('4.6h',z,vx)
    title = 'x=4.6, horizontal'
    plotnow(pname,title,'$z/D$','$u/U_{ref}$',z,vx,labels,linestyles=linestyles,markers=markers)

    fname = 'tjunc.00008.dat'
    x,y,z,vx,vy,vz,k,tau = getlocdata(cases,fname)
    pname = 'x4.6v'
    getexpData('4.6v',y,vx)
    title = 'x=4.6, vertical'
    plotnow(pname,title,'$y/D$','$u/U_{ref}$',y,vx,labels,linestyles=linestyles,markers=markers)
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
