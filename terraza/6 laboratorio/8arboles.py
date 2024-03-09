class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def altura_arbol(arbol):
    if not arbol.hijos:  # Si el árbol no tiene hijos, su altura es 1
        return 1
    alturas_hijos = [altura_arbol(hijo) for hijo in arbol.hijos]
    return 1 + max(alturas_hijos)

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

# Calcular la altura del árbol
altura = altura_arbol(raiz)
print("Altura del árbol:", altura)
