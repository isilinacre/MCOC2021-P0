# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from time import perf_counter
from numpy import ones
import scipy.sparse as sp
import scipy.sparse.linalg as lin
from numpy import double

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 

# -------------------------------------------------------------------------------------------------

def laplaciana(N, t):
    d = sp.eye(N, N, 1, dtype=t)
    return (2*sp.eye(N, dtype=t) - d - d.T)

# -------------------------------------------------------------------------------------------------
Ns = [2,4,10,15,20,30,35,40,45,50,55,60,65,80,100,150,170,200,250,400,500,600,800,1000,2000,5000,10000,15000,20000]

NCOR = 10 #numero de corridas que quiero que escriba el programa

for nc in range(NCOR): #recorro la cantidad de corridas entregado por la variable NCOR
    dts = []
    sol = []
    
    newfile = f"corrida_{nc}_matrizdispersa.txt" #creo un archivo .txt segun en la corrida que estoy 
    fid = open(newfile, "w") #abro el archivo creado

    for N in Ns: #recorro la lista Ns
        
        print(N)
    
        t1 = perf_counter() #funcion que me devuelve un float para tiempo en segundos 
        A = laplaciana(N, double)
        b = ones(N, double)
        Acsr = sp.csr_matrix(A)
        t2 = perf_counter() #funcion que me devuelve un float para tiempo en segundos 
        x = lin.spsolve(Acsr,b) #uso matmul para multiplicar las matrices creadas A y B        
        t3 = perf_counter()
        
        dtens = t2 - t1 #tiempo ensamblaje
        dtsol = t3 - t2 #tiempo solución
        
        linea = f"{N} {dtens} {dtsol} \n" #defino la linea a escribir
        fid.write(linea) #escribo la linea con N, dt y el uso de memoria total utilizado

        dts.append(dtens)
        sol.append(dtsol)
  
    fid.close()
    
    fid.close()

#print(f"Tiempo ensamblaje: {t2 - t1}")
#print(f"Tiempo solucion: {t3 - t2}")