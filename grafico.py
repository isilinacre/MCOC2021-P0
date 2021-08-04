# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:26:33 2021

@author: iplin
"""

from numpy import loadtxt
from scipy import matmul, rand
from time import perf_counter
from matplotlib import pyplot as plt
import matplotlib.ticker

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 

# -------------------------------------------------------------------------------------------------
NCOR = 10
dts_list = []
mems_list = []

for i in range(NCOR):
    fin = f"corrida_{i+1}.txt"
    datos = loadtxt(fin)
    print (datos)
    
    Ns = datos[:,0]
    dts = datos[:,1]
    mems = datos[:,2]
    
    dts_list.append(dts)
    mems_list.append(mems)

# -------------------------------------------------------------------------------------------------
plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.ylabel("Tiempo transcurrido (s)")

for l in range(NCOR):
    dts = dts_list[l]
    plt.loglog(Ns, dts,'-o')
    
y1_vals = [0.1e-3, 1e-3, 1e-2, 0.1, 1, 10, 60, 60*10]
y1_txt = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s","1 min","10 min"]
plt.yticks(y1_vals,labels=y1_txt)
x1_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
x1_txt = [""]*len(x1_vals) #agrego nada porque no quiero labels 
plt.xticks(x1_vals,x1_txt)
plt.grid()

plt.subplot(2,1,2)
plt.ylabel("Uso memoria")

for m in range(NCOR):
    mems = mems_list[m]
    plt.loglog(Ns,mems,'-o')

y2_vals = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 8*10**9, 10**11]
y2_txt = ['1 KB',"10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","8 GB","100 GB"]
plt.yticks(y2_vals,labels=y2_txt)
plt.axhline(y=8*10**9, xmin=0, color="r", linestyle = "--")
x2_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
x2_txt = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
plt.xticks(x2_vals,x2_txt,rotation=45)
plt.grid()

plt.tight_layout()
plt.savefig("Graficos")
plt.show()