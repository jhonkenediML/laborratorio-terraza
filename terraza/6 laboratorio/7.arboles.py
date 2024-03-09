class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(arbol):
    if not arbol.hijos:  # Verifica si el nodo actual no tiene hijos (es una hoja)
        return 0
    contador = 1  # Inicializa el contador con el nodo actual (interno)
    for hijo in arbol.hijos:  # Recorre los hijos del nodo actual
        contador += contar_nodos_internos(hijo)  # Recursivamente cuenta los nodos internos de cada hijo
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

# Contar la cantidad de nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print("Cantidad de nodos internos en el árbol:", cantidad_nodos_internos)
