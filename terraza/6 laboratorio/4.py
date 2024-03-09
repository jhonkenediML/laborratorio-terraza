import queue

class SistemaGestionTareas:
    def __init__(self):
        self.tareas_pendientes = queue.Queue()  # Inicializa una cola para almacenar las tareas pendientes

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.put(tarea)  # Agrega una nueva tarea a la cola
        print(f"Tarea '{tarea}' agregada.")

    def marcar_completada(self):
        if not self.tareas_pendientes.empty():
            tarea_completada = self.tareas_pendientes.get()  # Marca como completada y elimina la primera tarea de la cola
            print(f"Tarea '{tarea_completada}' marcada como completada.")
        else:
            print("No hay tareas pendientes para marcar como completadas.")

    def mostrar_proxima_tarea(self):
        if not self.tareas_pendientes.empty():
            print(f"Próxima tarea pendiente: {self.tareas_pendientes.queue[0]}")
        else:
            print("No hay tareas pendientes.")

# Ejemplo de uso
sistema_tareas = SistemaGestionTareas()
sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Preparar informe")
sistema_tareas.agregar_tarea("Enviar correo electrónico")

sistema_tareas.mostrar_proxima_tarea()
sistema_tareas.marcar_completada()

sistema_tareas.mostrar_proxima_tarea()