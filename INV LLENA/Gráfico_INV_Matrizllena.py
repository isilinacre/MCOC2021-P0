# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:26:33 2021

@author: iplin
"""

from numpy import loadtxt, mean, array
from scipy import matmul, rand
from time import perf_counter
from matplotlib import pyplot as plt
import matplotlib.ticker

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 

# -------------------------------------------------------------------------------------------------
NCOR = 10 #numero de corridas 
dts_list = []
sol_list = []
dts_last = []
sol_last = []

for i in range(NCOR): #recorro la cantidad de numero de corridas 
    fin = f"corrida_{i}_INV_matrizllena.txt" #recorro el archivo de texto i creado por timing_matmul  
    datos = loadtxt(fin) #cargo la informacion del archivo de texto "i" correspondiente 

    Ns = datos[:,0] #accedo a todos los datos de la primera matriz eligiendo solo los de la primera columna (N)
    dts = datos[:,1] #accedo a todos los datos de la primera matriz eligiendo solo los de la segunda columna (dt)
    sol = datos[:,2] #accedo a todos los datos de la primera matriz eligiendo solo los de la tercera columna (memoria)
    
    dts_list.append(dts) #agrego todos los datos de la 2° columna (dt) de la matriz i  
    sol_list.append(sol) #agrego todos los datos de la 3° columna (memoria) de la matriz i  
    
    dts_last.append(dts[-1])
    sol_last.append(sol[-1])

# -------------------------------------------------------------------------------------------------
dts_mean = mean(array(dts_last))  #Ordenes
sol_mean = mean(array(sol_last))
# -------------------------------------------------------------------------------------------------

plt.figure(1) #creo un grafico en blanco

plt.subplot(2,1,1) #creo 2 gráficos pero trabajo en el primero
plt.title("Rendimiento INV Matriz Llena") #le escribo el titulo principal a mis graficos
plt.ylabel("Tiempo de ensamblado (s)") #escribo el nombre correspondiente de la variable en eje y del primer grafico

for l in range(NCOR): #recorro la cantidad de numero de corridas 
    dts = dts_list[l] #denomino como dts a la variable en la posicion l de la lista dts_list para graficar
    plt.loglog(Ns, dts,'-o',linewidth=1,alpha=0.5) #grafico bilogaritmicamente N vs tiempo

plt.loglog(Ns,[dts_mean]*len(Ns),'--', color = 'blue') # O(cte)
plt.loglog(Ns,(dts_mean/Ns[-1])*(Ns),'--', color = 'orange') # O(N)
plt.loglog(Ns,(dts_mean/Ns[-1]**2)*(Ns**2),'--', color = 'green') # O(N2)
plt.loglog(Ns,(dts_mean/Ns[-1]**3)*(Ns**3),'--', color = 'red') # O(N3)
plt.loglog(Ns,(dts_mean/Ns[-1]**4)*(Ns**4),'--', color = 'pink') # O(N4)

y1_vals = [0.1e-3, 1e-3, 1e-2, 0.1, 1, 10, 60, 60*10] #valores de unidades de tiempo en eje y a escribir en este
y1_txt = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s","1 min","10 min"] #unidades de tiempo en eje y
plt.yticks(y1_vals,labels=y1_txt) #uso "ticks" para mostrar valores utilizados para mostrar ptos especificos en el grafico
x1_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000] #valores a utilizar como tamaños N de matriz
x1_txt = [""]*len(x1_vals) #agrego nada (literalmente) porque no quiero labels (texto en eje x)
plt.xticks(x1_vals,x1_txt) #nuevamente uso "ticks" para mostrar los valores especificados en el grafico
plt.ylim(0.1e-3/100,1000)
plt.grid() #hago la malla del grafico

plt.subplot(2,1,2) #creo 2 gráficos pero ahora trabajo en el segundo
plt.ylabel("Tiempo de solución (s)") #escribo el nombre correspondiente de la variable en eje y del segundo grafico
plt.xlabel("Tamaño matriz N") #nombre asignado al eje x

for m in range(NCOR): #recorro la cantidad de numero de corridas 
    sol = sol_list[m] #denomino como mems a la variable en la posicion m de la lista mems_list para graficar
    plt.loglog(Ns,sol,'-o',linewidth=1,alpha=0.5) #grafico bilogaritmicamente N vs memoria
    
plt.loglog(Ns,[sol_mean]*len(Ns),'--', color = 'blue', label='Constante') # O(cte)
plt.loglog(Ns,(sol_mean/Ns[-1])*(Ns),'--', color = 'orange', label='O(N)') # O(N)
plt.loglog(Ns,(sol_mean/Ns[-1]**2)*(Ns**2),'--', color = 'green', label='O(N^2)') # O(N2)
plt.loglog(Ns,(sol_mean/Ns[-1]**3)*(Ns**3),'--', color = 'red', label='O(N^3)') # O(N3)
plt.loglog(Ns,(sol_mean/Ns[-1]**4)*(Ns**4),'--', color = 'pink', label='O(N^4)') # O(N4)

y2_vals = [0.1e-3, 1e-3, 1e-2, 0.1, 1, 10, 60, 60*10] #valores de unidades de memoria en eje y
y2_txt = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s","1 min","10 min"] #unidades de memoria en eje y del segundo grafico
plt.yticks(y2_vals,labels=y2_txt) #uso "ticks" para mostrar valores utilizados para mostrar ptos especificos en el grafico
x2_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000] #valores utilizados como N (tamaño matriz)
x2_txt = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
plt.xticks(x2_vals,x2_txt,rotation=45) #roto los valores establecidos anteriormente en 45°
plt.ylim(0.1e-3/100,1000)
plt.legend()
plt.grid() #ploteo la malla del segundo grafico

plt.tight_layout() # se ajusta el grafico para que quede mas bonito y ordenado
plt.savefig("Grafico_INV_Matrizllena") #se guarda la foto del grafico en la carpeta donde se está corriendo este programa
plt.show() #muestra el grafico realizado