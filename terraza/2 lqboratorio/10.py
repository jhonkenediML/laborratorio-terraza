import numpy as np
def suma_de_matrices(matriz1,matriz2):
    try:
        b=np.array(matriz1)+np.array(matriz2)
        return b
    except ValueError: 
        return"son diferentes por lo cual no se pueden sumar"
a=[[1,2,3],[4,5,6],[7,8,9]]
c=[[9,8,7],[6,5,4],[3,2,1]]
print(suma_de_matrices(a,c))