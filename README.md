# MCOC2021-P0

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


# DESEMPEÑO MATMUL 

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

![Grafico](https://github.com/isilinacre/MCOC2021-P0/blob/0d5b9d29b503649b8b348aee4258e444f4bd9548/Graficos.png)
Figura 1. Gráfico realizado 

![Procesadores CPU](https://github.com/isilinacre/MCOC2021-P0/blob/03ee6ef289333b5bf5206116d33ae4fe3b3ab2ec/Procesadores%20CPU.png)
Figura 2. Procesadores una vez corrido el programa 


# DESEMPEÑO INV 

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.
--> El método de Numpy.linalg.inv() resuelve con la matriz A y la matriz I (identidad) utilizando el algoritmo solve. 
Por otro lado, el método de Scipy.linalg.inv() utiliza el algoritmo LU para invertir las matrices. Además, se trabajó con 
overwrite_a=False y overwrite_a=True, siendo overwrirte_a una función para sobre escribir sobre la matriz A dada. Utilizando 
la función overwrite_a=true, mejoró notablemente el rendimiento utilizado por el computador.

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en 
base al uso de procesadores y memoria observado durante las corridas.
--> El paralelismo y la estructura del caché incide positivamente en el desempeño de la memoria del computador, ya que 
al utilizar más de un procesador en el desarrollo del código, en mi caso utlizando 8.


# DESEMPEÑO SOLVE - EIGH

--> Se utilizaron matrices de dimensiones hasta 5000 para agilizar el tiempo de ejecución del código

¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? 
Se presentó en mi caso, que para el algortirmo SOLVE el tiempo de ejecución fue considerablemente menor en comparación 
con el algortirmo EIGH. Por otro lado, al ejecutar el algoritmo EIGH junto al parámetro "overwrite_a=True", el tiempo
de ejecución fue aún más lento. Esto es porque a pesar de que tengan el mismo orden, el algoritmo EIGH debe realizar
muchas más operaciones para llegar a una respuesta, en comparación con el algoritmo SOLVE.

¿Qué algoritmo gana (en promedio) en cada caso? 
Se tuvo que el algoritmo más rápido en promedio de tiempo de ejecución, fue SOLVE utilizando el dtype = single para
todos los casos, ya que este dtype utiliza menos memoria para la ejecución del codigo. 

![SOLVE - SINGLE](https://github.com/isilinacre/MCOC2021-P0/blob/6c02207312f02ddd98ddd200f3010e620092bd72/Entrega%204/Grafico_caso_A_single.png)

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

![CPU - EIGH](https://github.com/isilinacre/MCOC2021-P0/blob/6c02207312f02ddd98ddd200f3010e620092bd72/Entrega%204/F-EIGH.jpeg)
![CPU - SOLVE](https://github.com/isilinacre/MCOC2021-P0/blob/6c02207312f02ddd98ddd200f3010e620092bd72/Entrega%204/F-SOLVE.jpeg)


¿Que hay del uso de memoria (como crece)? 
El uso de memoria es lineal. Varía linealmente el tiempo transcurrido según la dimensión de la matriz ejecutada.
Por otro lado, en el caso que se utiliza el algoritmo SOLVE, se puede notar que la primera operación llevada a cabo,
es decir, invertir la matriz A y multiplicarla por el vector b (A^-1*b), utiliza más memoria que el resto de los 
parametros utilizados para calcular x. 

![MEMORIA - EIGH](https://github.com/isilinacre/MCOC2021-P0/blob/6c02207312f02ddd98ddd200f3010e620092bd72/Entrega%204/Grafico_caso_B_double_memoria.png)
![MEMORIA - SOLVE](https://github.com/isilinacre/MCOC2021-P0/blob/6c02207312f02ddd98ddd200f3010e620092bd72/Entrega%204/Grafico_caso_A_double_memoria.png)


# Matrices dispersas y complejidad computacional

La matriz laplaciana utilizada en el código de esta entrega

```python
def laplaciana(N, tipo = np.double):
    e = np.eye(N) - np.eye(N,N,1)
    return tipo(e + e.T)
```

La elección de la matriz laplaciana, cómo se ve reflejada en el desempeño y complejidad algorítmica mostrada?

Para el caso de la matriz llena (matriz cuyos valores incluye los términos cero), se puede ver del grafico que la complejidad algoritmica de ensamblaje de la 
matriz laplaciana es N^2 y tiempo de solución N^3. Se puede inferir que la complejidad del ensamblaje no afecta tanto dado que se tendria que mejorar el 
tiempo de solución antes que esta última. Al presentar un orden mayor, significa que tiene una mayor complejidad, por lo que se demora más en desarrollar el 
código, además de presentarse la posibilidad de no llevarse a cabo en algún momento por falta de memoria, por ejemplo. Por otro lado, dado esto, se tuvo que correr 
el programa hasta matrices de N = 10.000 como máximo, ya que con matrices mayores el tiempo de ensamblado y solución eran mayor a 2 minutos por corrida.  
Se adjunta el gráfico realizado para el rendimiento MATMUL de la matriz llena:

![Rendimiento MATMUL - Matriz llena](https://github.com/isilinacre/MCOC2021-P0/blob/8b30315875c2f156a74d37cd56af3813ac006af1/Grafico%20matriz%20llena.png)

Por otro lado, para el caso de la matriz dispersa (matriz modificada excluyendo los términos cero), fue notoria la diferencia en tiempos de solución, ya que a 
pesar de que el tiempo de ensamblado en términos de complejidad algoritmica fue la misma (N^2), los tiempos de solución bajaron una vez aplicando la función MATMUL
y una matriz "SPARSE" de formato tipo CSR, manteniendose en un rango entre 0.1 y 0.5 (ms) pudiéndose ver esto en el gráfico.
Además, se pudo concluir que el tiempo de solución cambia en comparación al tiempo de solución de la matriz llena, ya que se puede notar
que en este caso la complejidad está entre el orden N y N^2 versus el orden de N^3 de la matriz llena, por lo que en este caso (dispersa), se podría mejorar el tiempo de ensamblado para agilizar el tiempo y disminuir el orden de complejidad algoritmica. 

![Rendimiento MATMUL - Matriz dispersa](https://github.com/isilinacre/MCOC2021-P0/blob/8b30315875c2f156a74d37cd56af3813ac006af1/Grafico%20matriz%20dispersa.png)

En conclusión, se puede decir que mientras más grande sea el orden de la complejidad algoritmica, menos eficiente es el código escrito, por lo que se podría modificar 
la matriz laplaciana y ver si existe otra manera de escribirla para notar si mejora el rendimiento de la función MATMUL. Por otro lado, se pudo notar que mientras 
menos ceros tiene la matriz, menor es el orden de complejidad algoritmica lo que eficientiza el código y las funciones escritas.


# Matrices dispersas y complejidad computacional (PARTE II)

La matriz laplaciana utilizada en el código de esta entrega:

```python
def laplaciana(N, tipo = double):
    e = eye(N) - eye(N,N,1)
    return tipo(e + e.T)
```

Se presentan los gráficos realizados para hacer las respectivas comparaciones en las preguntas a continuación:

![Rendimiento Solve - Matriz llena](https://github.com/isilinacre/MCOC2021-P0/blob/main/SOLVE%20LLENA/Grafico_solve_Matrizllena.png)
Figura 1.- Solve Matriz Llena 

![Rendimiento Solve - Matriz dispersa](https://github.com/isilinacre/MCOC2021-P0/blob/main/SOLVE%20DISPERSA/Grafico%20Solve%20matriz%20dispersa.png)
Figura 2.- Solve Matriz Dispersa

![Rendimiento INV - Matriz llena](https://github.com/isilinacre/MCOC2021-P0/blob/main/INV%20LLENA/Grafico_INV_Matrizllena.png)
Figura 3.- INV Matriz Llena 

![Rendimiento INV - Matriz dispersa](https://github.com/isilinacre/MCOC2021-P0/blob/main/INV%20DISPERSA/Grafico%20INV%20matriz%20dispersa.png)
Figura 4.- INV  Matriz Dispersa

Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
Tal como se puede notar en las figuras 1 y 3, correspondientes a matrices llenas, se tiene que la complejidad algorítmica para el tiempo
de ensamblado, corresponde a un orden de N^2 , mientras que el tiempo de solución corresponde a un orden de N^3, tanto para la función
inv como para solve.
Por otro lado, para las matrices dispersas, correspondientes a las figuras 2 y 4, se puede notar una diferencia de complejidades algorítmicas 
entre ellas dadas las funciones utilizadas para cada una. Sin embargo, se puede ver que para la función inversa, la complejidad es muy alta
en comparación con solve para el mismo tipo de matriz. 
Se puede ver que las matrices llenas tienden a una complejidad a partir de matrices de dimensiones chicas como N = 50, tanto para ensamblado
como solución, mientras que para las matrices dispersas la tendencia a una complejidad comienza a partir de matrices de dimension muy 
grande. Además, se puede notar, tal como se comentó anteriormente, las matrices llenas son más eficientes que la matriz dispersa aplicada
a la inversa, pero menos eficiente que la matriz dispersa aplicada a "solve". 
* Por último, cabe destacar que para las matrices dispersas, dada su eficiencia, se corrieron hasta una dimensión de matriz equivalente a 
N = 20.000 para poder hacer una comparación entre matrices del mismo tipo, adicionando que mientras más prqueña la dimensión de la matriz, 
menos clara era su tendencia a una complejidad algoritmica. 

¿Cual parece la complejidad asintótica (para N → ∞)  para el ensamblado y solución en ambos casos y porqué?
La complejidad asintótica en caso de las matrices llenas, para el ensamblado las corridas tienden a un orden de N^2, mientras que
para la solución, las corridas tienden a un orden de N^3. Por otro lado, la complejidad asintótica para el caso de las matrices 
dispersas, depende de la función utilizada. Para el caso de utilizar "inv", la complejidad tiende a un orden N^4 para ambos casos, es decir, 
ensamblaje y solución, mientras que para "solve" la complejidad tiende a N. 
Para ambos casos, sus tendencias son para los respectivos ordenes ya que tienen una pendiente similar al orden al que se "acercan".

¿Como afecta el tamaño de las matrices al comportamiento aparente?
Para el caso de las matrices llenas, la tendencia comienza alrededor de dimensiones de N = 50 para todos los casos, mientras que para las
matrices dispersas, la tendencia de ensamblado comienza en N = 500 (aprox), mientras que para la solución en N = 1000 (aprox).
Dependiendo de cual sea el tipo de matriz y función que se esté aplicando, depende del tamaño de la matriz. Sin embargo, mientras más grande
es la dimensión de la matriz, baja la eficiencia de rendimiento del programa, ya que el uso de memoria utilizado es mayor.  

¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?
Para el caso de las matrices llenas, tanto para "inv" como "solve", las corridas se establecen constantes a partir de un N = 1000. Antes
de este valor, las corridas son poco estables desde N = 2 hasta aproximadamente N = 250. 
Por otro lado, para las matrices dispersas, las corridas para el tiempo de ensamblado utilizando "inv", por ejemplo, nunca se muestran 
estables antes de N = 20000, mientras que para "solve" se muestran más estables que el caso anteriormente mencionado, sin embargo, tampoco
es estable en su totalidad. Además, para el caso de los tiempos de solución ("inv"), se muestran estables las corridas a partir de N = 1000.

* Se reitera que para el caso de las matrices dispersas, se utilizaron dimensiones más grandes para poder analizar la complejidad algorítmica
* También, para el caso de las matrices dispersas utilizando la inversa, se utilizó CSC, ya que es más eficiente que CSR, utilizado para solve. 
* Se utilizaron para las matrices llenas, los casos más eficientes de entregas anteriores. 






