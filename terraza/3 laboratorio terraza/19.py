# ejercicio 19
def numeros_ordenados_y_sin_duplicados(conjunto):
    numeros_ordenados = sorted(list(conjunto))
    return set(numeros_ordenados)

conjunto_de_numeros = {5, 3, 8, 2, 5, 8, 1, 2, 9, 4}
conjunto_ordenado_sin_duplicados = numeros_ordenados_y_sin_duplicados(conjunto_de_numeros)
print(conjunto_ordenado_sin_duplicados)