from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def plotnow(fname,xlabel,ylabel,x,y,labels,ptype='line'):
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
    ax.legend(loc='best',fontsize=12)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def getdata(case,data,x,y,vx,vy,p,temp,sc1,sc2):
    data = np.loadtxt(case+'/'+data,skiprows =1)
    
    x.append(data[:,0])
    y.append(data[:,1])
    vx.append(data[:,2])
    vy.append(data[:,3])
    p.append(data[:,4])
    temp.append(data[:,5])
    sc1.append(data[:,6])
    sc2.append(data[:,7])
    
    return

def main():
    #Reported values by usrchk
    Re = 40000.
    utau = 4.5182E-02
    uavg = 1.0
    #Channel width
    H = 1.0 
    #Characteristic length
    L = 1.0
    nu = uavg*L/Re

    x = []
    y = []
    vx = []
    vy = []
    p = []
    temp = []
    sc1 = []
    sc2 = []
    #cases = ['coarse','coarse_6','coarse_8','wallResolved']
    cases = ['fine','fine_6','fine_8','wallResolved']
    #cases = ['wallResolved','../Re1M/wallResolved']
    cases = ['coarse','coarse_6','../../../../nek5k_RANS_Cases/funcy_MSFR/Re40k/coarse','wallResolved']
    cases = ['coarse','coarse_6','wallResolved']
    cases = ['coarse','coarse_6','wallResolved']

    #labels = ['coarse,lx1=4','coarse,lx1=6','coarse,lx1=8','wallResolved,lx1=8']
    #labels = ['fine,lx1=4','fine,lx1=6','fine,lx1=8','wallResolved,lx1=8']
    labels = ['coarse,GWF,lx1=4','coarse,GWF,lx1=6','coarse,SWF,lx1=4','wallResolved,lx1=8']
    labels = ['coarse,GWF,lx1=4','coarse,GWF,lx1=6','wallResolved,lx1=8']
    labels = ['lx1=4','lx1=6','wallResolved,lx1=8']
    #labels = ['Re=40k','Re=1M']

    pltname = 'plot1.dat'
    for i in range(len(cases)):
        getdata(cases[i],pltname,x,y,vx,vy,p,temp,sc1,sc2)

    labels = labels
    plotnow(cases[0]+'_U_x-0.5','$y$','$U$',y,vx,labels)
    plotnow(cases[0]+'_tke_x-0.5','$y$','$k$',y,sc1,labels)
    plotnow(cases[0]+'_tau_x-0.5','$y$','$\\tau$',y,sc2,labels)


    x = []
    y = []
    vx = []
    vy = []
    p = []
    temp = []
    sc1 = []
    sc2 = []
    pltname = 'plot2.dat'
    for i in range(len(cases)):
        getdata(cases[i],pltname,x,y,vx,vy,p,temp,sc1,sc2)

    labels = labels
    plotnow(cases[0]+'_U_y0.5','$x$','$U$',x,vx,labels)
    plotnow(cases[0]+'_tke_y0.5','$x$','$k$',x,sc1,labels)
    plotnow(cases[0]+'_tau_y0.5','$x$','$\\tau$',x,sc2,labels)

    x = []
    y = []
    vx = []
    vy = []
    p = []
    temp = []
    sc1 = []
    sc2 = []
    pltname = 'plot3.dat'
    for i in range(len(cases)):
        getdata(cases[i],pltname,x,y,vx,vy,p,temp,sc1,sc2)

    labels = labels
    plotnow(cases[0]+'_U_x0.5','$y$','$U$',y,vx,labels)
    plotnow(cases[0]+'_tke_x0.5','$y$','$k$',y,sc1,labels)
    plotnow(cases[0]+'_tau_x0.5','$y$','$\\tau$',y,sc2,labels)

    x = []
    y = []
    vx = []
    vy = []
    p = []
    temp = []
    sc1 = []
    sc2 = []
    pltname = 'plot4.dat'
    for i in range(len(cases)):
        getdata(cases[i],pltname,x,y,vx,vy,p,temp,sc1,sc2)
    labels = labels
    plotnow(cases[0]+'_U_x0','$y$','$U$',y,vx,labels)
    plotnow(cases[0]+'_tke_x0','$y$','$k$',y,sc1,labels)
    plotnow(cases[0]+'_tau_x0','$y$','$\\tau$',y,sc2,labels)
    
    # yplus = (H-y)*utau/nu
    # uplus = vx/utau
    # tkeplus = sc1/utau**2.
    # uplus = uplus[yplus>=0.9]
    # tkeplus = tkeplus[yplus>=0.9]
    # yplus = yplus[yplus>=0.9]

    # plotnow('uplus','$y^+$','$u^+$',[yplus],[uplus],labels,ptype='semilogx')
    # plotnow('tkeplus','$y^+$','$k^+$',[yplus],[tkeplus],labels,ptype='semilogx')
    
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
