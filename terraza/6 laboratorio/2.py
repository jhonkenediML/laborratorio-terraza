from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()  # Inicializa una cola utilizando deque

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        else:
            return None

    def tamaño(self):
        return len(self.items)

class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = Cola()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.encolar(pedido)
        print(f"Pedido '{pedido}' agregado a la cola de pedidos.")

    def procesar_pedido(self):
        if not self.cola_pedidos.esta_vacia():
            pedido_procesado = self.cola_pedidos.desencolar()
            print(f"Pedido '{pedido_procesado}' procesado.")
        else:
            print("No hay pedidos pendientes para procesar.")

    def mostrar_estado_cola(self):
        if not self.cola_pedidos.esta_vacia():
            print("Estado actual de la cola de pedidos:")
            for pedido in self.cola_pedidos.items:
                print(f"- {pedido}")
        else:
            print("La cola de pedidos está vacía.")

# Ejemplo de uso
sistema_pedidos = SistemaGestionPedidos()
sistema_pedidos.agregar_pedido("Pedido 1")
sistema_pedidos.agregar_pedido("Pedido 2")
sistema_pedidos.agregar_pedido("Pedido 3")

sistema_pedidos.mostrar_estado_cola()

sistema_pedidos.procesar_pedido()
sistema_pedidos.procesar_pedido()

sistema_pedidos.mostrar_estado_cola()