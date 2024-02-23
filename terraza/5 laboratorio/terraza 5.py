# 1 ejercicio
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

    def duplicar_nodos(self):
        nodo_actual = self.primero
        while nodo_actual is not None:
            nuevo_nodo = Nodo(nodo_actual.dato)
            nuevo_nodo.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            if nuevo_nodo.siguiente is not None:
                nuevo_nodo.siguiente.anterior = nuevo_nodo
            if nodo_actual == self.ultimo:
                self.ultimo = nuevo_nodo
            nodo_actual = nuevo_nodo.siguiente

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

# Duplicar los nodos
lista.duplicar_nodos()

# Imprimir la lista original hacia adelante
print("Lista original hacia adelante:")
lista.imprimir_adelante()

# Imprimir la lista duplicada hacia adelante
print("Lista duplicada hacia adelante:")
lista.imprimir_adelante()

# Imprimir la lista original hacia atrás
print("Lista original hacia atrás:")
lista.imprimir_atras()

# Imprimir la lista duplicada hacia atrás
print("Lista duplicada hacia atrás:")
lista.imprimir_atras()
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
# 7 ejerciccio
class pila:  #creamos una clse llamda pila
    def __init__(self):  #creamos una lista basia llamada items

        self.items=[]
    def esta_vasia(self): #funcion para saber si la pila esta vacia
        return len(self.items)==0
    def apilar (self,elementos): #funcion para apilar elementos
        self.items.append(elementos)
    def desapilar(self): #funcion para desapilar elementos
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("la pila esta vasia, Nose puede desapilar")
def decimal_a_binario(numero): #funcion para convertir decimal a binario
    pila=pila()

    while numero > 0: #mientras el numero sea mayor a 0
        residuo = numero % 2 #obtenemos el residuo del numero dividido entre 2
        pila.apilar(residuo) #apilamos el residuo
        numero = numero // 2#obtenemos el numero entero de la division entre 2

    binario = ""
    while not pila.esta_vacia():#mientras la pila no este vacia
        binario += str(pila.desapilar())#desapilamos el elemento de la pila y lo convertimos en un string

    return binario


# Ejemplo de uso del codigo para observa el desarroollo
numero_decimal = 42
numero_binario = decimal_a_binario(numero_decimal)

print("Número decimal:", numero_decimal)
print("Número binario:", numero_binario)  
#9 ejercio
class Pila:
    def __init__(self):#inicializa la pila
        self.items = []#inicializa la pila vacia

    def apilar(self, item):#funcion para apilar
        self.items.append(item)

    def desapilar(self):#funcion para desapilar
        if not self.esta_vacia():#si la pila no esta vacia
            return self.items.pop()#    devuelve el elemento de la pila

    def esta_vacia(self):#funcion para saber si la pila esta vacia
        return len(self.items) == 0#devuelve el tamanio de la pila


def validar_expresion(expresion):#funcion para validar la expresion
    pila = Pila()#crea una pila

    for caracter in expresion:#recorre la expresion
        if caracter in "([{":#si el caracter es un parentesis, corchete o llave
            pila.apilar(caracter)
        elif caracter in ")]}":#si el caracter es un parentesis, corchete o llave
            pila.apilar(caracter)#apila el caracter
        elif caracter in ")]}":#si el caracter es un parentesis, corchete o llave
            if pila.esta_vacia() or not coincide_operador(pila.desapilar(), caracter):
                return False
#si la pila no esta vacia y no coincide el parentesis, corchete o llave
    return pila.esta_vacia()#devuelve la pila


def coincide_operador(apertura, cierre):# funcion para validar el parentesis, corchete o llave
    if apertura == "(" and cierre == ")":# valida el parentesis
        return True# devuelve verdadero
    elif apertura == "[" and cierre == "]":# valida el corchete
        return True# devuelve verdadero
    elif apertura == "{" and cierre == "}":# valida el llave
        return True# devuelve verdadero
    else:#
        return False#   devuelve falso


# Ejemplo de uso
expresion = "(4+(3-5))/7"
es_correcto = validar_expresion(expresion)

if es_correcto:
    print("La expresión está correctamente anidada.")
else:
    print("La expresión no está correctamente anidada.")
#11 ejercicio
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0


def eliminar_duplicados(pila):
    pila_unica = Pila()
    elementos_unicos = set()

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_unicos:
            pila_unica.apilar(elemento)
            elementos_unicos.add(elemento)

    return pila_unica


# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(2)
pila.apilar(4)
pila.apilar(1)

print("Pila original:", pila.items)

pila_sin_duplicados = eliminar_duplicados(pila)

print("Pila sin duplicados:", pila_sin_duplicados.items)
#13 ejercicio
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0


def es_palindromo(palabra):
    pila = Pila()

