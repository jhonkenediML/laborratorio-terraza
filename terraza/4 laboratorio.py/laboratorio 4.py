
# EJERCICIO 1
# Validar la edad de un usuario.
def validar_edad(nombre, edad):
    assert isinstance(edad, int), f"La edad de {nombre} debe ser un número entero"
    # assert 0 <= edad <= 100, f"La edad de {nombre} debe estar entre 0 y 100 años"
print(validar_edad("Diego", 129))


# EJERCICIO 2
#. Verificar el tipo de dato de una variable.
variable = 42
assert isinstance(variable, int),"La variable no es un entero"

# EJERCICIO 3
# Validar el rango de una calificación.
def validar_calificacion(calificacion):
    assert 0 <= calificacion <= 20, "La calificación debe estar en el rango de 0 a 20"
print(validar_calificacion(134))


# EJERCICIO 4
#. Asegurar que una lista no esté vacía.
my_list = [1, 2, 3]
assert len(my_list) > 0, "La lista está vacía"
# EJERCICIO 5
#Validar la igualdad de dos objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __eq__(self, otro):
        if isinstance(otro, Persona):
            return self.nombre == otro.nombre and self.edad == otro.edad
        return False
# # Ejemplo de uso
person1 = Persona("Diego", 10)
person2 = Persona("Diego", 10)
person3 = Persona("Sheyla", 15)

print(person1 == person2)  
print(person1 == person3) 


# EJERCICIO 6
 # 6 Asegurar que un ciclo while se ejecuta al menos una vez
contador=0
while contador < 10:
    contador+=1
    assert contador == 10,"el contador no se repite"

# EJERCICIO 7
def suma(a, b):
    return a + b
# Llamamos la función
resultado = suma(10, 30)
assert resultado == 40, "La función suma no está retornando el valor esperado"

print("La función suma devuelve el valor esperado:", resultado)
#Ejercicio 8
#8
variable=20+20
assert variable>0,"El resultado no es un número positivo"
# ejercicio 10
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
# ejrcicio 12
#Longitud de la Lista

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

    def longitud(self):
        contador = 0
        actual = self.inicio
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

longitud = lista.longitud()
print("Longitud de la lista:", longitud)
#ejercicio 14
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