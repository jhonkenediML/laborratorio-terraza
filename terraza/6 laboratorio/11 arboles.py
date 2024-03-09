class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_maximo(arbol):
    if not arbol.hijos:  # Si el árbol no tiene hijos, devuelve su propio nodo como máximo
        return arbol
    maximo = arbol  # Inicializa el máximo con el nodo actual
    for hijo in arbol.hijos:  # Recorre los hijos del nodo actual
        maximo_hijo = encontrar_maximo(hijo)  # Encuentra el máximo en cada subárbol
        if maximo_hijo.valor > maximo.valor:  # Compara con el máximo actual
            maximo = maximo_hijo
    return maximo

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(10)
hijo1 = Nodo(5)
hijo2 = Nodo(15)
nieto1 = Nodo(20)
nieto2 = Nodo(7)

raiz.hijos.extend([hijo1, hijo2])
hijo2.hijos.append(nieto1)
hijo2.hijos.append(nieto2)

# Encontrar el nodo con el valor máximo en el árbol
nodo_maximo = encontrar_maximo(raiz)
print("Nodo con valor máximo en el árbol:", nodo_maximo.valor)
