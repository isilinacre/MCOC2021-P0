# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
Ns = [2,4,8,10,20,40,50,100,200,500,1000,2000,5000,10000]

NCOR = 10 #numero de corridas que quiero que escriba el programa

for nc in range(NCOR): #recorro la cantidad de corridas entregado por la variable NCOR
    dts = []
    mems = []
    
    newfile = f"corrida_{nc+1}.txt" #creo un archivo .txt segun en la corrida que estoy 
    fid = open(newfile, "w") #abro el archivo creado

    for N in Ns: #recorro la lista Ns
        A = rand(N,N) #creo una matriz A al azar de NxN entre 0 y 1
        B = rand(N,N) #creo una matriz B al azar de NxN entre 0 y 1
       
        t1 = perf_counter() #funcion que me devuelve un float para tiempo en segundos 
        
        C = A@B #uso matmul para multiplicar las matrices creadas A y B
    
        t2 = perf_counter() #funcion que me devuelve un float para tiempo en segundos 
        
        usomemoriatotal = A.nbytes + B.nbytes + C.nbytes #calculo la memoria total utilizada para la creacion de matrices
        
        dt = t2 - t1 #diferencia en segundos
        
        linea = f"{N} {dt} {usomemoriatotal} \n" #defino la linea a escribir
        fid.write(linea) #escribo la linea con N, dt y el uso de memoria total utilizado
        
        dts.append(dt)
        mems.append(usomemoriatotal) 
    
        #print(f"N={N} dt={dt} s mem = {usomemoriatotal} bytes flops = (N**3/dt) flops/s")
    
    fid.close()

