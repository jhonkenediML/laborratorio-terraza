#10. Desarrollar el código de buscar nodo en la lista enlazada simple
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.inicio:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, valor):
        actual = self.inicio
        while actual:
            if actual.dato == valor:
                return actual
            actual = actual.siguiente
        return None

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Buscar un nodo con valor 2
nodo_buscado = lista.buscar(2)
if nodo_buscado:
    print("Nodo encontrado con valor:", nodo_buscado.dato)
else:
    print("Nodo no encontrado")
