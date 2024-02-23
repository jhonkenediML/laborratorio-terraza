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


def decimal_a_binario(numero):
    pila = Pila()

    while numero > 0:
        residuo = numero % 2
        pila.apilar(residuo)
        numero = numero // 2

    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())

    return binario


# Ejemplo de uso
numero_decimal = 42
numero_binario = decimal_a_binario(numero_decimal)

print("Número decimal:", numero_decimal)
print("Número binario:", numero_binario)

