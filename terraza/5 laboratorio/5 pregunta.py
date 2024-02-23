class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def invertir(self):
        nodo_actual = self.cabeza
        nodo_anterior = None
        while nodo_actual is not None:
            siguiente_nodo = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_anterior
            nodo_anterior = nodo_actual
            nodo_actual = siguiente_nodo
        self.cabeza = nodo_anterior

    def imprimir_adelante(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

    def imprimir_atras(self):
        nodo_actual = self.cabeza
        nodos_reversos = []
        while nodo_actual is not None:
            nodos_reversos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        nodos_reversos.reverse()
        for valor in nodos_reversos:
            print(valor)

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar(100)
lista.insertar(200)
lista.insertar(500)
lista.insertar(2)
lista.insertar(36)

print("Lista original:")
lista.imprimir_adelante()

lista.invertir()

print("Lista invertida:")
lista.imprimir_adelante()

print("Lista invertida hacia atrás:")
lista.imprimir_atras()