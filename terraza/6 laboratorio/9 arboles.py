class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def profundidad_nodo(raiz, nodo, profundidad_actual=0):
    if raiz is None:
        return 0  # Si la raíz es nula, la profundidad es 0
    if raiz == nodo:
        return profundidad_actual  # Si se encuentra el nodo, se devuelve la profundidad actual
    for hijo in raiz.hijos:
        profundidad = profundidad_nodo(hijo, nodo, profundidad_actual + 1)  # Búsqueda recursiva en los hijos
        if profundidad != 0:
            return profundidad  # Si se encuentra en un hijo, se devuelve la profundidad
    return 0  # Si no se encuentra el nodo, se retorna 0

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(1)
hijo1 = Nodo(2)
hijo2 = Nodo(3)
nieto1 = Nodo(4)
nieto2 = Nodo(5)

raiz.hijos.extend([hijo1, hijo2])
hijo1.hijos.append(nieto1)
hijo2.hijos.append(nieto2)

# Calcular la profundidad de un nodo específico (por ejemplo, el nodo con valor 4)
nodo_buscado = nieto1
profundidad_nodo_buscado = profundidad_nodo(raiz, nodo_buscado)
print(f"Profundidad del nodo {nodo_buscado.valor}: {profundidad_nodo_buscado}")
