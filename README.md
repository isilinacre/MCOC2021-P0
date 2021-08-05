# MCOC2021-P0

# Desempeño MATMUL

* ¿Cómo difiere del gráfico del profesor/ayudante?
Mi grafico difiere principalmente en los tiempos transcurridos de las diferentes corridas, como se puede ver en la primera de estas. 
Se puede notar que las primeras corridas del profesor/ayudante tienen un tiempo transcurrido de 0.1 (ms) mientras que mi gráfico muestra un tiempo
transcurrido de 0.1 (s). 
Por otra parte se puede ver en el gráfico del profesor/ayudante que para tamaños de matrices empleadas entre N = 50 y N = 1000, el tiempo transcurrido
es mayor al presentado en el mio. 

* ¿A qué se pueden deber las diferencias en cada corrida?
Pueden ser diferentes dado que los procesadores son distintos y tienen diferente capacidad entre computadores. 
Por otro lado, al correr el programa, el computador puede estar utilizando memoria en otras cosas, lo que puede hacer más o menos lento el proceso de cálculo 
de las matrices alterando el tiempo transcurrido de este.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
El uso de memoria es igual a un factor, que es el tamaño de cada numero por la cantidad de numeros, siendo del orden de N^2.
En caso del tiempo, el orden de la multiplicacion de matrices debiese ser del orden N^3, explicando por qué este no es "lineal".

* ¿Qué versión de python está usando?
Python 3.8.5 - MSC v.1916 64 bit (AMD64)

* ¿Qué versión de numpy está usando?
Numpy 1.19.2

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 
Se adjunta foto de los procesadores trabajando durante una corrida. Se puede notar como aumenta el trabajo de los procesadores una vez corrido el programa. 

![Grafico](https://github.com/isilinacre/MCOC2021-P0/blob/main/Graficos.png)
![Procesadores CPU](https://github.com/isilinacre/MCOC2021-P0/blob/main/Procesadores%20CPU.png)




