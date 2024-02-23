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