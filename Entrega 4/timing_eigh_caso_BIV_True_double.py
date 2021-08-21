# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:09:58 2021

@author: iplin
"""

from time import perf_counter
from numpy import eye, ones
from scipy.linalg import eigh
from numpy import single, double

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 
# -------------------------------------------------------------------------------------------------

def laplaciana(N, dtype = double):
    e = eye(N) - eye(N,N,1)
    return dtype(e + e.T)

# -------------------------------------------------------------------------------------------------
Ns = [2,4,10,15,20,30,35,40,45,50,55,60,65,80,100,150,170,200,250,400,500,600,800,1000,2000,5000]
NCOR = 10

fid = open("Corrida_caso_BIV_True_double.txt", "w") #abro el archivo creado

for nc in range(NCOR): #recorro la cantidad de corridas entregado por la variable NCOR
    fid.write(f"Corrida {nc} \n")
    print(nc)

    for N in Ns: #recorro la lista Ns
        A = laplaciana(N, dtype = double)
        
        t1 = perf_counter()
        w,h = eigh(A, overwrite_a=True, driver="evr")
        t2 = perf_counter()
        
        #print(x)
        
        dt_solve = t2 - t1
        
        bytes_total = A.nbytes + w.nbytes + h.nbytes
        
        linea = f"{N} {dt_solve} {bytes_total} \n" #defino la linea a escribir
        fid.write(linea) #escribo la linea con N, dt y el uso de memoria total utilizado
        
    fid.write("\n")

fid.write("FINAL \n")
fid.close()

print(f"Tiempo solve: {dt_solve} (s)")
print(f"Memoria: {bytes_total}")