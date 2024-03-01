class UndoSystem:
    def __init__(self):
        self.actions = []  # Pila para almacenar las acciones realizadas
        self.undo_actions = []  # Pila para almacenar las acciones para deshacer

    def do_action(self, action):
        # Realizar la acción y almacenarla en la pila de acciones
        print(f"Realizando la acción: {action}")
        self.actions.append(action)

    def undo(self):
        if self.actions:
            # Sacar la última acción realizada de la pila de acciones
            last_action = self.actions.pop()
            # Almacenar la acción en la pila de acciones para deshacer
            self.undo_actions.append(last_action)
            print(f"Deshaciendo la acción: {last_action}")
        else:
            print("No hay acciones para deshacer")

    def redo(self):
        if self.undo_actions:
            # Sacar la última acción deshecha de la pila de acciones para deshacer
            last_undo_action = self.undo_actions.pop()
            # Realizar la acción nuevamente
            print(f"Rehaciendo la acción: {last_undo_action}")
            self.actions.append(last_undo_action)
        else:
            print("No hay acciones para rehacer")


# Ejemplo de uso
undo_system = UndoSystem()
undo_system.do_action("Editar texto")
undo_system.do_action("Eliminar elemento")
undo_system.do_action("Guardar archivo")

# Deshacer una acción
undo_system.undo()

# Rehacer una acción
undo_system.redo()