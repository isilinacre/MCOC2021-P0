# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:31:47 2021

@author: iplin
"""

from matplotlib import pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 
# -------------------------------------------------------------------------------------------------

NCOR = 10 #numero de corridas 
#file = open("Corrida_N.txt", "r")

nombrestxt = ["Corrida_caso_AI_double.txt",
              "Corrida_caso_AII_double.txt",
              "Corrida_caso_AIII_double.txt",
              "Corrida_caso_AIV_double.txt",
              "Corrida_caso_AV_double.txt",
              "Corrida_caso_AVI_double.txt",
              "Corrida_caso_AVII_double.txt"]

dataDict = {}

for nombre in nombrestxt:
    
    print(nombre,"\n")
    
    Ns_list = []
    dts_list = [] #tiempos
    mems_list = []

    with open(nombre) as f:
        contenido = f.readlines()
    
    for linea in contenido:
        #print(linea.split())
        
        if len(linea.split()) == 2:
            Ns = []
            dts = [] #tiempos
            mems = []
        
        if (len(linea.split()) == 1 and linea.split()[0] == "FINAL") or len(linea.split()) == 0:
            pass
            
        elif len(linea.split()) == 3:
            Ns.append(int(linea.split()[0]))
            dts.append(float(linea.split()[1]))
            mems.append(int(linea.split()[2]))
        
        else:
            Ns_list.append(Ns)
            dts_list.append(dts) #agrego todos los datos de la 2° columna (dt) de la matriz i  
            mems_list.append(mems) #agrego todos los datos de la 3° columna (memoria) de la matriz i  
    
    data = np.mean(np.array(dts_list), axis = 0)
    dataDict[nombre]=data
    

    print(data)
    print(data.shape)
    
plt.figure(1) #creo un grafico en blanco

plt.subplot(1,1,1) #creo 2 gráficos pero trabajo en el primero
plt.title("Rendimiento Solve A double") #le escribo el titulo principal a mis graficos
plt.ylabel("Tiempo transcurrido (s)") #escribo el nombre correspondiente de la variable en eje y del primer grafico
plt.xlabel("Tamaño matriz N")

for nombre in nombrestxt:  
    print(nombre)
    dts = dataDict[nombre] #denomino como dts a la variable en la posicion l de la lista dts_list para graficar
    plt.loglog(Ns, dts,'-o',label=nombre) #grafico bilogaritmicamente N vs tiempo
    
y1_vals = [0.1e-3, 1e-3, 1e-2, 0.1, 1, 10, 60, 60*10] #valores de unidades de tiempo en eje y a escribir en este
y1_txt = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s","1 min","10 min"] #unidades de tiempo en eje y
plt.yticks(y1_vals,labels=y1_txt) #uso "ticks" para mostrar valores utilizados para mostrar ptos especificos en el grafico
#x1_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000] #valores a utilizar como tamaños N de matriz
#x1_txt = [""]*len(x1_vals) #agrego nada (literalmente) porque no quiero labels (texto en eje x)
#plt.xticks(x1_vals,x1_txt) #nuevamente uso "ticks" para mostrar los valores especificados en el grafico
#plt.grid() #hago la malla del grafico
x2_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000] #valores utilizados como N (tamaño matriz)
x2_txt = ["10","20","50","100","200","500","1000","2000","5000","10000"]
plt.xticks(x2_vals,x2_txt,rotation=45) #roto los valores establecidos anteriormente en 45°
plt.legend()

plt.tight_layout() # se ajusta el grafico para que quede mas bonito y ordenado
plt.savefig("Grafico_caso_A_double") #se guarda la foto del grafico en la carpeta donde se está corriendo este programa
plt.show() #muestra el grafico realizado


