# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:09:58 2021

@author: iplin
"""

from time import perf_counter
from numpy import zeros
from scipy.linalg import inv #especificar que estoy usando este (scipy)
from numpy import half, single, double, longdouble

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 
# -------------------------------------------------------------------------------------------------

def laplaciana(N, dtype):
    A=zeros((N,N), dtype = dtype)
    
    for i in range(N): #se va a recorrer la mitad de la matriz 
        A[i,i] = 2 
        
        for j in range(max(0,i-2),i): #para que no me quede un -1 en las esquinas 
            if abs(i-j) == 1:
                A[i,j] = -1
                A[j,i] = -1
    return(A)

# -------------------------------------------------------------------------------------------------


Ns = [2,4,10,15,20,30,35,40,45,50,55,60,65,80,100,150,170,200,250,400,500,600,800,1000,2000,5000,10000]

NCOR = 10 #numero de corridas que quiero que escriba el programa

fid = open("Corrida_Scipy_double.txt", "w") #abro el archivo creado

for nc in range(NCOR): #recorro la cantidad de corridas entregado por la variable NCOR
    fid.write(f"Corrida {nc} \n")

    for N in Ns: #recorro la lista Ns
        t1 = perf_counter()
        A = laplaciana(N, dtype = double) #el hald me tira lo mismo que el float16

        t2 = perf_counter()
        Am1 = inv(A,overwrite_a=False)
        t3 = perf_counter()
        
        dt_inversion = t3- t2 #cuanto se demora en invertir la matriz - ESTE es el que hay que hacer 
        bytes_total = A.nbytes + Am1.nbytes
        
        print(dt_inversion)
        print(bytes_total)
        
        linea = f"{N} {dt_inversion} {bytes_total} \n" #defino la linea a escribir
        fid.write(linea) #escribo la linea con N, dt y el uso de memoria total utilizado

    fid.write("\n")

fid.write("FINAL \n")
fid.close()

print(f"Uso memoria - dtype double: {bytes_total}")
print(f"Tiempo de inversión - dtype double: {dt_inversion} (ms)")