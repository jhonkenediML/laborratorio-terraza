import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
fila,columna=a.shape
fila_central=fila//2
columna_central=columna//2
print(f"{a[fila_central,columna_central]}")
