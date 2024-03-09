
# ejercicio 14
def numeros_no_duplicados(conjunto_numeros):
    """
    Esta función recibe un conjunto de números
    y devuelve un conjunto con los números que no están duplicados.
    """
    numeros_no_duplicados = {numero for numero in conjunto_numeros if list(conjunto_numeros).count(numero) == 1}
    return numeros_no_duplicados

# Ejemplo de uso:
conjunto_numeros = {5, 2, 8, 1, 9, 3, 5, 2, 8}

resultado = numeros_no_duplicados(conjunto_numeros)
print(f"Números no duplicados: {resultado}")