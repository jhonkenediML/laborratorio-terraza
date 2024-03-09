# ejercicio 4
def interseccion_entre_conjuntos(conjunto1, conjunto2):
    """
    Esta función recibe dos conjuntos de números
    y devuelve un conjunto con los números que están en ambos conjuntos.
    """
    interseccion = conjunto1.intersection(conjunto2)
    return interseccion

# Ejemplo de uso:
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado = interseccion_entre_conjuntos(conjunto_a, conjunto_b)
print(f"Intersección entre los conjuntos: {resultado}")