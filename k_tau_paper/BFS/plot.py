from cycler import cycler
import math
import numpy as np
import os
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plplot(fname,xlabel,ylabel,x,y,pos,labels,lstyles,mrks):
    default_cycler = (cycler(color=['k','b','r','c','g','m'])*\
                      cycler(linestyle=['-'])*cycler(marker=['']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    
    c = int(len(y)/2)
    r = int(len(y)/c)

    #reshape
    if(fname=='U'):
        fig,axs = plt.subplots(r,c,sharey=True,sharex=True,figsize=(12,8))
    else:
        fig,axs = plt.subplots(r,c,sharey=True,figsize=(12,8))
    
    k =0
    for i in range(r):
        for j in range(c):
            for l in range(len(y[k])):
                axs[i,j].plot(x[k][l],y[k][l],linestyle=lstyles[l],marker=mrks[l],linewidth=1.5,label=labels[l])
            axs[i,j].set_title('$x/H=$'+pos[k],fontsize=12)
            axs[i,j].grid()
            axs[i,j].set_ylim([0.0,3.0])
            if(i+1==r and j+1==c):
                axs[i,j].legend(loc='best',fontsize=10)

            if(i+1==r):
                axs[i,j].set_xlabel(xlabel,fontsize=15)
            if(j==0):
                axs[i,j].set_ylabel(ylabel,fontsize=15)
            axs[i,j].tick_params(axis='both',labelsize=12)
            k+=1
    
    # for ax in axs.flat:
    #     ax.set_xlabel('$u/U$',fontsize=15)
    #     ax.set_ylabel('$y/H$',fontsize=15)
    #     ax.tick_params(axis='both',labelsize=12)

    # for ax in axs.flat:
    #     ax.label_outer()

    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return


def plotnow2(fname,x,y,labels,lstyles,mrks):
    default_cycler = (cycler(color=['k','b','r','c']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    fig = plt.figure(figsize=(7,5))
    
    r = int(len(y))
    fig,axs = plt.subplots(figsize=(7,5))

    k=0
    #print(len(y),len(y[k]),y[k)
    for i in range(r):
        for l in range(len(y[i])):
            if(i==0):
                axs.plot(x[i][l],y[i][l],linestyle=lstyles[l],marker=mrks[l],linewidth=1.5,label=labels[l])
            else:
                axs.plot(x[i][l],y[i][l],linestyle=lstyles[l],marker=mrks[l],linewidth=1.5)
            
        
    axs.grid()
    axs.set_ylim([0,3])
    axs.legend(loc='best',fontsize=12)
    axs.set_xlabel('$u/U$',fontsize=15)
    axs.set_ylabel('$y/H$',fontsize=15)
    axs.tick_params(axis='both',labelsize=12)

    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def plotnow(fname,title,xlabel,ylabel,x,y,labels,lstyles,mrks,ptype='line',lims=True):
    default_cycler = (cycler(color=['k','b','r','c','g','m'])*\
                      cycler(linestyle=['-'])*cycler(marker=['']))
    plt.rc('lines',linewidth=1)
    plt.rc('axes',prop_cycle=default_cycler)
    fig = plt.figure(figsize=(7,5))
    if(lims):
        fig = plt.figure(figsize=(3,5))
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
    #ax.set_title(title,fontsize=15)
    if(lims):
        ax.set_ylim([0.0,3.0])
    ax.legend(loc='best',fontsize=12)
    fig.savefig(fname+'.png',quality=100,\
                bbox_inches='tight',dpi=100)
    plt.close()
    return

def getdata(fname,x,y,vx,vy,p,temp,sc1,sc2,i,yfac,uadd,ifadd):
    if(fname=="med" or fname=="coarse" or fname=='of3'):
        getOFData(x,y,vx,vy,p,temp,sc1,sc2,i,fname,uadd,ifadd)
    else:
        if(i<9):
            fname = fname+"/bfs.0000"+str(i+1)+".dat"
        else:
            fname = fname+"/bfs.000"+str(i+1)+".dat"
        print(fname)
        data = np.loadtxt(fname,skiprows=1)
        x.append(data[:,0]*yfac)
        y.append(data[:,1]*yfac+1.0)
        if(ifadd):
            vx.append(data[:,2]+uadd)
        else:
            vx.append(data[:,2])
        vy.append(data[:,3])
        p.append(data[:,4])
        temp.append(data[:,5]*2)
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

def getExpData(pos,uadd,ifadd):
    pos = float(pos)
    posstr = 'expData/data'+'%1.1f'%(pos)+'.dat'
    data = np.loadtxt(posstr,delimiter=',',skiprows=1)
        
    yu = data[:,0]
    yk = yu
    if(ifadd):
        u = data[:,1]+uadd
    else:
        u = data[:,1]
    k = data[:,2]
    return u,yu,k,yk

def getOFData(x,y,vx,vy,p,temp,sc1,sc2,i,dname,uadd,ifadd):
    if(dname=="med"):
        fname="openFoam/BFS_med/data/data"+str(i)+".csv"
    elif(dname=='coarse'):
        fname="openFoam/BFS_coarse/data/data"+str(i)+".csv"
    else:
        fname="openFoam/BFS_coarse2/data/data"+str(i)+".csv"
    
    data = np.loadtxt(fname,delimiter=",",skiprows=1)
    y.append(data[:,2]*4+1)
    if(ifadd):
        vx.append(data[:,4]+uadd)
    else:
        vx.append(data[:,4])
    sc1.append(data[:,-2])
    sc2.append(data[:,-1])

    x.append(data[:,1])
    vy.append(data[:,5])
    p.append(data[:,0]) #dummy
    temp.append(data[:,0]) #dummy
    
    return

def getcfdata(fname,x,temp,i,yfac):
    if(i<9):
        fname1 = fname+"/bfs.0000"+str(i+1)+".dat"
    else:
        fname1 = fname+"/bfs.000"+str(i+1)+".dat"
        
    if(i+1<9):
        fname2 = fname+"/bfs.0000"+str(i+2)+".dat"
    else:
        fname2 = fname+"/bfs.000"+str(i+2)+".dat"

    data1 = np.loadtxt(fname1,skiprows=1)
    data2 = np.loadtxt(fname2,skiprows=1)
    x.append(np.concatenate((data2[:,0],data1[:,0]))*yfac)
    
    temp.append(np.concatenate((data2[:,5],data1[:,5]))*2)
    
    return

def getexpcfdata(x,temp):
    data = np.loadtxt('exp_cf.dat',skiprows=1)
    x.append(data[:,0])
    temp.append(data[:,1])
    return

def getofcfdata(x,temp):
    fname = 'openFoam/BFS_med/line.xy'
    data = np.loadtxt(fname,skiprows=1)

    fname='openFoam/BFS_med/line0.xy'
    data0 = np.loadtxt(fname,skiprows=1)
    x.append(np.concatenate((data0[:,0],data[:,0]))*4)
    temp.append(np.concatenate((data0[:,1],data[:,1]))*-2)
    return

def main():
    
    n = 22
    lbl = "x="
    all_labels = ["-4","-2","-1","0","1","1.5","2","2.5","3","4","5",\
                  "5.5","6","6.5","7","8","10","12","14","16","20","32"]
    poslabels = ["-4","0","1.5","2.5","5","6","8","10"]
    uadd = [0,0,0,0,0,0,0,0]
    ifadd = False

    poslabels = ["2","4","6.5","8","14","32"]
    uadd = [0.5,1,1.5,2,2.5,3]
    ifadd = True

    #all_labels = poslabels
    
    cases = ['wallResolved_ktau/tplots','wallResolved_ktau_scaled/tplots','openFoam','openFoam2','of3']
    cases = ['wallResolved_ktau/tplots','wallResolved_omega/tplots','med']

    labels = ['$k-\\tau$','reg $k-\\omega$','OF $k-\\omega$ SST (fine)','OF $k-\\omega SST (med)$','OF $k-\\omega SST (coarse)$']
    labels = ['$k-\\tau$','$k-\\omega \, (reg)$','OF $k-\\omega \, SST$','OF $k-\\omega SST (med)$']

    lstyles = ['','-','--','--','--','--']
    mrks = ['.','','','','','']

    yfac = [4,4,1,1,1,1]

    plplot_u_x = []
    plplot_u_y = []
    plplot_k_x = []
    plplot_k_y = []

    for j in range(n):
        i=-1
        if(all_labels[j] in poslabels):
            i = poslabels.index(all_labels[j])
            print(i,poslabels[i],all_labels[j])
        else:
            i = -1
            print("not found")
            
        uexp,yuexp,kexp,kyexp = getExpData(all_labels[j],uadd[i],ifadd)
        x,y,vx,vy,p,temp,sc1,sc2 = clearDat()
        for c in range(len(cases)):
            fname = cases[c]
            getdata(fname,x,y,vx,vy,p,temp,sc1,sc2,j,yfac[c],uadd[i],ifadd)

        if(i!=-1):
            title = "x/H="+poslabels[i]
            pname = "Umean_x="+poslabels[i]            
            xdata = vx.copy()
            xdata.insert(0,uexp)
            ydata = y.copy()
            ydata.insert(0,yuexp)
            lbs = labels.copy()
            lbs.insert(0,'Exp (D&S)')
            #plotnow(pname,title,"$U/U_{ref}$","$y/H$",xdata,ydata,lbs,lstyles,mrks)
        
            plplot_u_x.append(xdata)
            plplot_u_y.append(ydata)

            pname = "k_x="+poslabels[i]            
            xdata = sc1.copy()
            xdata.insert(0,kexp)
            ydata = y.copy()
            ydata.insert(0,kyexp)
            lbs = labels.copy()
            lbs.insert(0,'Exp (D&S)')
            #plotnow(pname,title,"$k/U_{ref}^2$","$y/H$",xdata,ydata,lbs,lstyles,mrks)
            plplot_k_x.append(xdata)
            plplot_k_y.append(ydata)

            
    plotnow2('Uarr',plplot_u_x,plplot_u_y,lbs,lstyles,mrks)
    #plot parallel
    plplot('U','$u/U$','$y/H$',plplot_u_x,plplot_u_y,poslabels,lbs,lstyles,mrks)
    plplot('k','$k/U^2$','$y/H$',plplot_k_x,plplot_k_y,poslabels,lbs,lstyles,mrks)

    #plot skin friction
    x,y,vx,vy,p,temp,sc1,sc2 = clearDat()
    getexpcfdata(x,temp)
    
    fname = cases[0]
    getcfdata(fname,x,temp,22,yfac[0])

    fname = cases[1]
    getcfdata(fname,x,temp,22,yfac[1])

    getofcfdata(x,temp)
        
    pname = 'cf'
    lbs = labels.copy()
    lbs.insert(0,'Exp (D&S)')
    plotnow(pname,'','$x/H$','$C_f$',x,temp,lbs,lstyles,mrks,lims=False)

    #Find reattachment point
    for i in range(1,len(x)):
        xmin = 6.2
        xmax= 6.8
        temp[i] = temp[i][x[i]>xmin]
        x[i] = x[i][x[i]>xmin]
        temp[i] = temp[i][x[i]<xmax]
        x[i] = x[i][x[i]<xmax]
        print(x[i],temp[i])
        c = np.polyfit(x[i],temp[i],1)
        f = lambda z:z*c[0]+c[1]
        print("soln:",fsolve(f,[xmin,xmax]))
    return

if __name__=="__main__":
    starttime = time.time()
    main()
    print('--- Code ran in %s seconds ---'%(time.time()-starttime))
