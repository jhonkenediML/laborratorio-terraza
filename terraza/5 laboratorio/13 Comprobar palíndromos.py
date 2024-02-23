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
    pila = Pila()#crea una pila

    # Apilar los caracteres de la palabra
    for caracter in palabra:#recorre la palabra
        pila.apilar(caracter)#apila el caracter

    # Desapilar y comparar con los caracteres originales
    palabra_inversa = ""
    while not pila.esta_vacia():#mientras la pila no este vacia
        palabra_inversa += pila.desapilar()#desapila el elemento

    return palabra_inversa.lower() == palabra.lower()#    devuelve el tamanio de la pila


# Ejemplo de uso
palabra = "reconocer"
es_pal = es_palindromo(palabra)#devuelve el tamanio de la pila

if es_pal:
    print(f'La palabra "{palabra}" es un palíndromo.')#    devuelve el tamanio de la pila
else:
    print(f'La palabra "{palabra}" no es un palíndromo.')#    devuelve el tamanio de la pila
