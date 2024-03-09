#ejercicio 5
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1 - conjunto2

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado_diferencia = diferencia_entre_conjuntos(conjunto_a, conjunto_b)

print(f"Diferencia entre {conjunto_a} y {conjunto_b}: {resultado_diferencia}")