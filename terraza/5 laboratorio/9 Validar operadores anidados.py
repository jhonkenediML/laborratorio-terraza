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