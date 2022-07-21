# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:01:14 2022

@author: nsaini
"""

import math
import numpy as np
from cycler import cycler
import matplotlib.pyplot as plt
import os
import time
from scipy.optimize import curve_fit
import re

def extFloat(line):
    return re.findall(r"[-+]?(?:\d*\.\d+|\d+)",line)

def initializeData():
    y=[]
    u=[]
    uu=[]
    vv=[]
    uv=[]
    k=[]
    return y,u,uu,vv,uv,k

def addToData(data,y,u,uu,vv,uv,k):
    y.append(float(data[1]))
    u.append(float(data[2]))
    uu.append(float(data[4])/1000.)
    vv.append(float(data[5])/1000.)
    uv.append(float(data[6])/1000.)
    k.append(0.5*(uu[-1]+vv[-1])*1.5)
    
def main():
    if not os.path.exists("expData"):
        os.makedirs("expData")
    
    file = open('exp_data_full.dat','r')
    lines = file.readlines()
    file.close()
    
    loc = 0.
    y=[]
    u=[]
    uu=[]
    vv=[]
    uv=[]
    k=[]
    
    for l in range(len(lines)):
        line = lines[l]
        if(line.find('X/H=')!=-1):
            loc = float(extFloat(line)[0])
            y,u,uu,vv,uv,k=initializeData()
        if(line.find('Y/H')!=-1):
            l+=1
            line = lines[l]
            data = extFloat(line)
            while (len(data)==11):
                addToData(data, y, u, uu, vv, uv, k)
                l+=1
                line = lines[l]
                data = extFloat(line)
            yp = np.asarray(y)
            up = np.asarray(u)
            kp = np.asarray(k)
            locstr = "%1.1f"%(loc)
            np.savetxt('expData/data'+locstr+'.dat',np.c_[yp,up,kp],delimiter=',',header='x/H='+locstr+' y, u, k')
        
    return

if __name__ == "__main__":
    starttime = time.time()
    main()
    print("--- Code ran in %s seconds ---"%(time.time()-starttime))
