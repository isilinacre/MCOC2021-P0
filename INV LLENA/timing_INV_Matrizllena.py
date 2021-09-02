# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from time import perf_counter
from numpy import eye
from scipy.linalg import inv #especificar que estoy usando este (scipy)
from numpy import double

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 

# -------------------------------------------------------------------------------------------------

def laplaciana(N, tipo = double):
    e = eye(N) - eye(N,N,1)
    return tipo(e + e.T)

# -------------------------------------------------------------------------------------------------
Ns = [2,4,10,15,20,30,35,40,45,50,55,60,65,80,100,150,170,200,250,400,500,600,800,1000,2000,5000,10000,15000]

NCOR = 10

for nc in range(NCOR): 
    dts = []
    sol = []
    print(nc) 
    
    newfile = f"corrida_{nc}_INV_matrizllena.txt" #creo un archivo .txt segun en la corrida que estoy 
    fid = open(newfile, "w") #abro el archivo creado

    for N in Ns:
    
        t1 = perf_counter() 
        A = laplaciana(N, double)
        t2 = perf_counter() 
        Am1 = inv(A,overwrite_a=False)
        t3 = perf_counter()
        
        dtens = t2 - t1 #tiempo ensamblaje
        dtsol = t3 - t2 #tiempo solución
        
        linea = f"{N} {dtens} {dtsol} \n" #defino la linea a escribir
        fid.write(linea) #escribo la linea con N, dt y el uso de memoria total utilizado

        dts.append(dtens) #agrego los datos obtenidos a la lista dts
        sol.append(dtsol) #agrego los datos obtenidos a la lista sol
  
    fid.close()


