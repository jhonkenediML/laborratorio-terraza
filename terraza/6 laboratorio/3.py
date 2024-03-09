class Cola:
    def __init__(self):
        self.items = []  # Inicializa una lista para almacenar los elementos de la cola

    def esta_vacia(self):
        return len(self.items) == 0  # Verifica si la cola está vacía

    def encolar(self, item):
        self.items.append(item)  # Agrega un elemento al final de la cola

    def desencolar(self):
        if not self.esta_vacia():  # Verifica si la cola no está vacía
            return self.items.pop(0)  # Elimina y devuelve el primer elemento de la cola (FIFO)

    def tamaño(self):
        return len(self.items)  # Devuelve el tamaño actual de la cola

class SistemaGestionTareas:
    def __init__(self):
        self.tareas_pendientes = Cola()  # Inicializa una instancia de la clase Cola para almacenar las tareas pendientes

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.encolar(tarea)  # Agrega una nueva tarea a la cola de tareas pendientes

    def marcar_completada(self):
        if not self.tareas_pendientes.esta_vacia():  # Verifica si hay tareas pendientes
            tarea_completada = self.tareas_pendientes.desencolar()  # Marca como completada y elimina la primera tarea de la cola

    def mostrar_proxima_tarea(self):
        if not self.tareas_pendientes.esta_vacia():  # Verifica si hay tareas pendientes
            print(f"Próxima tarea pendiente: {self.tareas_pendientes.items[0]}")  # Muestra la próxima tarea pendiente
        else:
            print("No hay tareas pendientes.")