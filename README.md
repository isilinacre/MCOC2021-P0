^^3# MCOC2021-P0


# Mi computador principal

* Marca/modelo: Asus VivoBook X413FA - BV807T

* Tipo: Notebook

* Año adquisición: 2021

* Procesador:
- Marca/Modelo: Intel Core i5-10210U
- Velocidad Base: 1.6 GHz
- Velocidad Máxima: 4,20 GHz
- Numero de núcleos: 4
- Humero de hilos: 8
- Arquitectura: AMD64
- Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
- Tamaño de las cachés del procesador

- L1: 256KB
- L2: 1MB
- L3: 6MB

* Memoria
- Total: 8GB
- Tipo memoria: DDR4-2666
- Velocidad: 2667 MHz
- Numero de (SO)DIMM: 2

* Tarjeta Gráfica
- Marca / Modelo: Intel UHD Graphics 620
- Memoria dedicada: 0MB (Integrada)
- Resolución: 1366 x 768

* Disco 1:
- Marca: WDC
- Tipo: SSD
- Tamaño: 256GB
- Particiones: 0
- Sistema de archivos: NTFS

Dirección MAC de la tarjeta wifi: AC-12-03-8C-44-C1

Dirección IP (Interna, del router): 192.168.1.111

Dirección IP (Externa, del ISP): 201.189.149.58

Proveedor internet: Fibra óptica Movistar


#Desempeño MATMUL

¿Cómo difiere del gráfico del profesor/ayudante? 
Mi grafico difiere principalmente en los tiempos transcurridos de las diferentes corridas, como se puede ver en la primera 
de estas. Se puede notar que las primeras corridas del profesor/ayudante tienen un tiempo transcurrido de 0.1 (ms) 
mientras que mi gráfico muestra un tiempo transcurrido de 0.1 (s). 
Por otra parte se puede ver en el gráfico del profesor/ayudante que para tamaños de matrices empleadas entre N = 50 y 
N = 1000, el tiempo transcurrido es mayor al presentado en el mio.

¿A qué se pueden deber las diferencias en cada corrida? 
Pueden ser diferentes dado que los procesadores son distintos y tienen diferente capacidad entre computadores. 
Por otro lado, al correr el programa, el computador puede estar utilizando memoria en otras cosas, lo que puede hacer 
más o menos lento el proceso de cálculo de las matrices alterando el tiempo transcurrido de este.

El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? 
El uso de memoria es igual a un factor, que es el tamaño de cada numero por la cantidad de numeros, siendo del orden de N^2. 
En caso del tiempo, el orden de la multiplicacion de matrices debiese ser del orden N^3, explicando por qué este no 
es "lineal".

¿Qué versión de python está usando? Python 3.8.5 - MSC v.1916 64 bit (AMD64)

¿Qué versión de numpy está usando? Numpy 1.19.2

Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador 
durante alguna corrida para confirmar. Se adjunta foto de los procesadores trabajando durante una corrida. 
Se puede notar como aumenta el trabajo de los procesadores una vez corrido el programa.

![Grafico](https://github.com/isilinacre/MCOC2021-P0/blob/main/Grafico.png)
Figura 1. Gráfico realizado 

![Procesadores CPU](https://github.com/isilinacre/MCOC2021-P0/blob/main/Procesadores%20CPU.png)
Figura 2. Procesadores una vez corrido el programa 


#Desempeño INV 

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.
--> El método de Numpy.linalg.inv() resuelve con la matriz A y la matriz I (identidad) utilizando el algoritmo solve. 
Por otro lado, el método de Scipy.linalg.inv() utiliza el algoritmo LU para invertir las matrices. Además, se trabajó con 
overwrite_a=False y overwrite_a=True, siendo overwrirte_a una función para sobre escribir sobre la matriz A dada. Utilizando 
la función overwrite_a=true, mejoró notablemente el rendimiento utilizado por el computador.

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en 
base al uso de procesadores y memoria observado durante las corridas.
--> El paralelismo y la estructura del caché incide positivamente en el desempeño de la memoria del computador, ya que 
al utilizar más de un procesador en el desarrollo del código, en mi caso utlizando 8.


# Desempeño SOLVE - EIGH

--> Se utilizaron matrices de dimensiones hasta 5000 para agilizar el tiempo de ejecución del código

¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? 
Se presentó en mi caso, que para el algortirmo SOLVE el tiempo de ejecución fue considerablemente menor en comparación 
con el algortirmo EIGH. Por otro lado, al ejecutar el algoritmo EIGH junto al parámetro "overwrite_a=True", el tiempo
de ejecución fue aún más lento. Esto es porque a pesar de que tengan el mismo orden, el algoritmo EIGH debe realizar
muchas más operaciones para llegar a una respuesta, en comparación con el algoritmo SOLVE.

¿Qué algoritmo gana (en promedio) en cada caso? 
Se tuvo que el algoritmo más rápido en promedio de tiempo de ejecución, fue SOLVE utilizando el dtype = single para
todos los casos, ya que este dtype utiliza menos memoria para la ejecución del codigo. 

![SOLVE - SINGLE](https://github.com/isilinacre/MCOC2021-P0/blob/main/Entrega%204/Grafico_caso_A_single.png)


¿Depende del tamaño de la matriz? 
En gran parte de los casos, sobretodo con matrices de mayor dimensión, el tiempo de ejecución fue más lento que 
en matrices entre N = 2 y N = 20, por ejemplo. Por lo tanto sí depende del tamaño de la matriz, sobre todo por ser 
de orden N al cubo.

¿A que se puede deber la superioridad de cada opción? 
Como ya se explicó anteriormente, utilizar el algoritmo SOLVE para ejecutar operaciones, utiliza un menor 
tiempo dado que las operaciones son más cortas. Además, como se puede ver en los gráficos, mediante SOLVE 
el caso más rápido fue utilizando una matriz definida positiva, tanto para el dtype single como double. 
Por otro lado, utilizando el algortimo EIGH, se tuvo que la opción más rápida fue para el tercer caso, es decir,
utilizando el driver (evd), además de utilizar el dtype single. 
Estas superioridades se pueden deber a que utilizan una menor capacidad de los procesadores, por lo que los tiempos
de ejecución son menores. 

¿Su computador usa más de un proceso por cada corrida? 
Sí, utiliza los ocho procesadores tanto para resolver mediante SOLVE como EIGH.

![CPU - EIGH](https://github.com/isilinacre/MCOC2021-P0/blob/main/Entrega%204/F-EIGH.jpeg)
![CPU - SOLVE](https://github.com/isilinacre/MCOC2021-P0/blob/main/Entrega%204/F-SOLVE.jpeg)


¿Que hay del uso de memoria (como crece)? 
El uso de memoria es lineal. Varía linealmente el tiempo transcurrido según la dimensión de la matriz ejecutada.
Por otro lado, en el caso que se utiliza el algoritmo SOLVE, se puede notar que la primera operación llevada a cabo,
es decir, invertir la matriz A y multiplicarla por el vector b (A^-1*b), utiliza más memoria que el resto de los 
parametros utilizados para calcular x. 

![MEMORIA - EIGH](https://github.com/isilinacre/MCOC2021-P0/blob/main/Entrega%204/Grafico_caso_B_double_memoria.png)
![MEMORIA - SOLVE](https://github.com/isilinacre/MCOC2021-P0/blob/main/Entrega%204/Grafico_caso_A_double_memoria.png)


# Matrices dispersas y complejidad computacional

La matriz laplaciana utilizada en el código de esta entrega

```python
def laplaciana(N, tipo = np.double):
    e = np.eye(N) - np.eye(N,N,1)
    return tipo(e + e.T)
```

La elección de la matriz laplaciana, cómo se ve reflejada en el desempeño y complejidad algorítmica mostrada?

Para el caso de la matriz llena, se puede ver del grafico que la complejidad algoritmica del ensamblaje de la laplaciana es N**2 y tiempo
de solución N**3. Se puede inferir que la complejidad del ensamblaje no afecta tanto dado que se tendria que mejorar la solucion antes
que esta última. Al presentar un orden mayor, significa que tiene una mayor complejidad por lo que se demora más en desarrollar, además
de presentarse la posibilidad de no llevarse a cabo el código. Por otro lado, dado esto, se tuvo que correr el programa hasta matrices
de N = 10.000 como máximo, ya que con matrices mayores el tiempo de ensamblado y solución eran mayor a 2 minutos por corrida.  
Se adjunta el gráfico realizado para el rendimiento MATMUL de la matriz llena:

![Rendimiento MATMUL - Matriz llena](-)

Por otro lado, para el caso de la matriz dispersa, fue notoria la diferencia en tiempos de solución, ya que a pesar de que el tiempo de 
ensamblado en términos de complejidad algoritmica fue la misma (N**2), los tiempos de solución una vez aplicando la función MATMUL
y una matriz "SPARSE" de formato tipo CSR, bajaron, manteniendose en un rango entre 0.1 y 0.5 (ms), por lo que se puede ver en la figura,
además de poder extraer que el tiempo de solución cambia en comparación al tiempo de solución de la matriz llena, ya que se puede notar
que en este caso la complejidad está entre el orden N y N**2, por lo que en este caso, lo que se podría mejorar es el tiempo de ensamblado
para agilizar el tiempo y disminuir el orden de complejidad algoritmica. 

![Rendimiento MATMUL - Matriz dispersa](-)


















