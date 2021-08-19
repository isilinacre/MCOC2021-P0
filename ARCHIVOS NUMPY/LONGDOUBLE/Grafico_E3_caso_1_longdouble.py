# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:31:47 2021

@author: iplin
"""

from matplotlib import pyplot as plt

#import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning) 
#warnings.filterwarnings("ignore", category=RuntimeWarning) 
# -------------------------------------------------------------------------------------------------

NCOR = 10 #numero de corridas 
Ns_list = []
dts_list = [] #tiempos
mems_list = []

with open("Corrida_Numpy_longdouble.txt") as f:
    contenido = f.readlines()

for linea in contenido:
    #print(linea.split())
    
    if len(linea.split()) == 2:
        Ns = []
        dts = [] #tiempos
        mems = []
    
    if (len(linea.split()) == 1 and linea.split()[0] == "FINAL"):
        pass
        
    elif len(linea.split()) == 3:
        Ns.append(int(linea.split()[0]))
        dts.append(float(linea.split()[1]))
        mems.append(int(linea.split()[2]))
    
    else:
        Ns_list.append(Ns)
        dts_list.append(dts) #agrego todos los datos de la 2° columna (dt) de la matriz i  
        mems_list.append(mems) #agrego todos los datos de la 3° columna (memoria) de la matriz i  

plt.figure(1) #creo un grafico en blanco

plt.subplot(2,1,1) #creo 2 gráficos pero trabajo en el primero
plt.title("Rendimiento INVERSA - dtype longdouble") #le escribo el titulo principal a mis graficos
plt.ylabel("Tiempo transcurrido (s)") #escribo el nombre correspondiente de la variable en eje y del primer grafico

for l in range(NCOR): #recorro la cantidad de numero de corridas 
    dts = dts_list[l] #denomino como dts a la variable en la posicion l de la lista dts_list para graficar
    plt.loglog(Ns, dts,'-o') #grafico bilogaritmicamente N vs tiempo
    
y1_vals = [0.1e-3, 1e-3, 1e-2, 0.1, 1, 10, 60, 60*10] #valores de unidades de tiempo en eje y a escribir en este
y1_txt = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s","1 min","10 min"] #unidades de tiempo en eje y
plt.yticks(y1_vals,labels=y1_txt) #uso "ticks" para mostrar valores utilizados para mostrar ptos especificos en el grafico
x1_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000] #valores a utilizar como tamaños N de matriz
x1_txt = [""]*len(x1_vals) #agrego nada (literalmente) porque no quiero labels (texto en eje x)
plt.xticks(x1_vals,x1_txt) #nuevamente uso "ticks" para mostrar los valores especificados en el grafico
plt.grid() #hago la malla del grafico

plt.subplot(2,1,2) #creo 2 gráficos pero ahora trabajo en el segundo
plt.ylabel("Uso memoria") #escribo el nombre correspondiente de la variable en eje y del segundo grafico
plt.xlabel("Tamaño matriz N") #nombre asignado al eje x

for m in range(NCOR): #recorro la cantidad de numero de corridas 
    mems = mems_list[m] #denomino como mems a la variable en la posicion m de la lista mems_list para graficar
    plt.loglog(Ns,mems,'-o') #grafico bilogaritmicamente N vs memoria

y2_vals = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 8*10**9, 10**11] #valores de unidades de memoria en eje y
y2_txt = ['1 KB',"10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","8 GB","100 GB"] #unidades de memoria en eje y del segundo grafico
plt.yticks(y2_vals,labels=y2_txt) #uso "ticks" para mostrar valores utilizados para mostrar ptos especificos en el grafico
plt.axhline(y=8*10**9, xmin=0, color="r", linestyle = "--") #se establece una linea horizontal en 8GB, maxima capacidad de la RAM de mi computador
x2_vals = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000] #valores utilizados como N (tamaño matriz)
x2_txt = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
plt.xticks(x2_vals,x2_txt,rotation=45) #roto los valores establecidos anteriormente en 45°
plt.grid() #ploteo la malla del segundo grafico

plt.tight_layout() # se ajusta el grafico para que quede mas bonito y ordenado
plt.savefig("Grafico_dtype_longdouble") #se guarda la foto del grafico en la carpeta donde se está corriendo este programa

plt.show() #muestra el grafico realizado


