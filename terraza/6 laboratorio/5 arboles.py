class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_arbol(arbol):
    if not arbol:  # Verifica si el nodo actual es nulo
        return 0  # Si es nulo, no hay nodos que contar
    contador = 1  # Inicializa el contador con el nodo actual
    for hijo in arbol.hijos:  # Recorre los hijos del nodo actual
        contador += contar_nodos_arbol(hijo)  # Recursivamente cuenta los nodos de cada hijo
    return contador

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

# Contar la cantidad de nodos en el árbol
cantidad_nodos = contar_nodos_arbol(raiz)
print("Cantidad de nodos en el árbol:", cantidad_nodos)
