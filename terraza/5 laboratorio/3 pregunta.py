# 3 ejercicio
# Definir la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# Definir la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def insertar_nodo(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if posicion == 1:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        else:
            nodo_actual = self.primero
            contador = 1
            while contador < posicion - 1 and nodo_actual is not None:
                nodo_actual = nodo_actual.siguiente
                contador += 1
            if nodo_actual is None:
                print("Posición inválida")
                return
            nuevo_nodo.anterior = nodo_actual
            nuevo_nodo.siguiente = nodo_actual.siguiente
            if nodo_actual.siguiente is not None:
                nodo_actual.siguiente.anterior = nuevo_nodo
            nodo_actual.siguiente = nuevo_nodo
            if nodo_actual == self.ultimo:
                self.ultimo = nuevo_nodo

    def imprimir_adelante(self):
        nodo_actual = self.primero
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def imprimir_atras(self):
        nodo_actual = self.ultimo
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.anterior

# Crear una instancia de la lista enlazada
lista = ListaEnlazada()

# Agregar nodos a la lista
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.agregar_nodo(4)
lista.agregar_nodo(5)

# Insertar un nuevo nodo en la posición 3 con el dato 15
lista.insertar_nodo(15, 3)

# Imprimir la lista hacia adelante
print("Lista hacia adelante:")
lista.imprimir_adelante()

# Imprimir la lista hacia atrás
print("Lista hacia atrás:")
lista.imprimir_atras()