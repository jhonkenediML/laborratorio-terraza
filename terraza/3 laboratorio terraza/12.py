#ejercicio 12
def numeros_ordenados_descendente(conjunto_numeros):
    """
    Esta función recibe un conjunto de números
    y devuelve un conjunto con los números ordenados de mayor a menor.
    """
    numeros_ordenados = set(sorted(conjunto_numeros, reverse=True))
    return numeros_ordenados

# Ejemplo de uso:
s = {5, 2, 8, 1, 9, 3}
print(numeros_ordenados_descendente(s))