#ejercicio 1
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_en_conjunto(conjunto):
    primos = set()
    for numero in conjunto:
        if es_primo(numero):
            primos.add(numero)
    return primos

conjunto_de_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_de_primos = numeros_primos_en_conjunto(conjunto_de_numeros)
print(conjunto_de_primos)