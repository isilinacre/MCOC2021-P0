# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:57:52 2021

@author: iplin
"""

#from scipy.sparse import lil_matrix, sparse 
import scipy.sparse as sp 
from numpy import zeros, float64

#def laplaciana(N, dtype):
 #   A = lil_matrix((N,N), dtype = dtype)
    
  #  for i in range(N): #se va a recorrer la mitad de la matriz 
   #     A[i,i] = 2 
        
    #    for j in range(max(0,i-2),i): #para que no me quede un -1 en las esquinas 
     #       if abs(i-j) == 1:
      #          A[i,j] = -1
       #         A[j,i] = -1
    #return(A)


def laplaciana(N, t):
    d = sp.eye(N,N,1,dtype=t)
    #e = sparse.eye(N, dtype = t) - sparse.eye(N, N, 1, dtype = t)
    #return(e+e.T)
    return (2*sp.eye(N,dtype=t) - d - d.T)


