import numpy as np

def submatriz_mayor_suma(matriz):
    matriz_np = np.array(matriz)
    filas, columnas = matriz_np.shape
    mejor_suma = float('-inf')
    mejor_submatriz = None

    for i in range(filas):
        for j in range(columnas):
            for k in range(i, filas):
                for l in range(j, columnas):
                    suma_actual = np.sum(matriz_np[i:k+1, j:l+1])
                    if suma_actual > mejor_suma:
                        mejor_suma = suma_actual
                        mejor_submatriz = matriz_np[i:k+1, j:l+1]

    return mejor_submatriz.tolist()

# Ejemplo de uso
matriz_ejemplo = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

resultado = submatriz_mayor_suma(matriz_ejemplo)
print("Submatriz de mayor suma:")
print(resultado)