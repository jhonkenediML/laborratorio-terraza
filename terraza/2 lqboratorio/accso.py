import numpy as np
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Obtener las dimensiones de la matriz
filas, columnas = matriz.shape

# Calcular las coordenadas del elemento central
fila_central = filas // 2
columna_central = columnas // 2

# Acceder al elemento central
elemento_central = matriz[fila_central, columna_central]

# Imprimir el resultado
print(f"Elemento central de la matriz: {elemento_central}")