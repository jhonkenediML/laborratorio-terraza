class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_minimo(arbol):
    if not arbol.hijos:  # Si el árbol no tiene hijos, devuelve su propio nodo como mínimo
        return arbol
    minimo = arbol  # Inicializa el mínimo con el nodo actual
    for hijo in arbol.hijos:  # Recorre los hijos del nodo actual
        minimo_hijo = encontrar_minimo(hijo)  # Encuentra el mínimo en cada subárbol
        if minimo_hijo.valor < minimo.valor:  # Compara con el mínimo actual
            minimo = minimo_hijo
    return minimo

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(10)
hijo1 = Nodo(5)
hijo2 = Nodo(15)
nieto1 = Nodo(3)
nieto2 = Nodo(7)

raiz.hijos.extend([hijo1, hijo2])
hijo1.hijos.append(nieto1)
hijo1.hijos.append(nieto2)

# Encontrar el nodo con el valor mínimo en el árbol
nodo_minimo = encontrar_minimo(raiz)
print("Nodo con valor mínimo en el árbol:", nodo_minimo.valor)
