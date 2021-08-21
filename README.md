# MCOC2021-P0

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








