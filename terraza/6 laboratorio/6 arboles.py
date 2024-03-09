class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_hoja(arbol):
    if not arbol.hijos:  # Verifica si el nodo actual no tiene hijos (es una hoja)
        return 1  # Si es una hoja, se cuenta como un nodo hoja
    contador = 0
    for hijo in arbol.hijos:  # Recorre los hijos del nodo actual
        contador += contar_nodos_hoja(hijo)  # Recursivamente cuenta las hojas de cada hijo
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

# Contar la cantidad de nodos hoja en el árbol
cantidad_nodos_hoja = contar_nodos_hoja(raiz)
print("Cantidad de nodos hoja en el árbol:", cantidad_nodos_hoja)
