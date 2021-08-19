# MCOC2021-P0

# Desempeño INV

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 

--> El método de Numpy.linalg.inv() resuelve con la matriz A y la matriz I (identidad) utilizando el algoritmo 
solve. Por otro lado, el método de Scipy.linalg.inv() utiliza el algoritmo LU para invertir las matrices.
Además, se trabajó con overwrite_a=False y overwrite_a=True, siendo overwrirte_a una función para sobre escribir
sobre la matriz A dada. Utilizando la función overwrite_a=true, mejoró notablemente el rendimmiento utilizado por 
el computador.  

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? 
Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 

--> El paralelismo y la estructura del caché incide positivamente en el desempeño de la memoria del computador, ya que
al utilizar más de un procesador en el desarrollo del código, en mi caso utlizando 8. 

