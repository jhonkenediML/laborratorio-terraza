#ejercicio 6
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    """
    Esta función recibe dos conjuntos de números
    y devuelve un conjunto con los números que están en el segundo conjunto pero no en el primero.
    """
    diferencia = conjunto2 - conjunto1
    return diferencia

# Ejemplo de uso:
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado = diferencia_entre_conjuntos(conjunto_a, conjunto_b)
print(f"Diferencia entre los conjuntos: {resultado}")