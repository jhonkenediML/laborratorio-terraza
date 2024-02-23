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
#ejemplo 3
def numeros_divisibles(conjunto, divisor):
    divisibles = set()
    for numero in conjunto:
        if numero % divisor == 0:
            divisibles.add(numero)
    return divisibles


conjunto_de_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3


conjunto_divisible = numeros_divisibles(conjunto_de_numeros, divisor)


print(f"Números en el conjunto {conjunto_de_numeros} divisibles por {divisor}: {conjunto_divisible}")
#ejemplo 5
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1 - conjunto2

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado_diferencia = diferencia_entre_conjuntos(conjunto_a, conjunto_b)

print(f"Diferencia entre {conjunto_a} y {conjunto_b}: {resultado_diferencia}")
#ejemplo 7
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def anagramas_en_conjunto(conjunto_palabras):
    anagramas = set()

    for palabra1 in conjunto_palabras:
        for palabra2 in conjunto_palabras:
            if palabra1 != palabra2 and son_anagramas(palabra1, palabra2):
                anagramas.add(palabra1)
                anagramas.add(palabra2)

    return anagramas

conjunto_de_palabras = {"roma", "amor", "perro", "roper", "casa", "saca"}
conjunto_de_anagramas = anagramas_en_conjunto(conjunto_de_palabras)
print(conjunto_de_anagramas)
#ejemplo 9
def palabras_longitud(conjunto, longitud):
    return {palabra for palabra in conjunto if len(palabra) == longitud}
#ejmlpo 11
def numeros_ordenados_menor_a_mayor(conjunto):
    return {num for num in conjunto if list(conjunto) == sorted(conjunto)}
#ejemplo 13
def numeros_duplicados(conjunto):
    duplicados = set()
    for num in conjunto:
        if list(conjunto).count(num) > 1:
            duplicados.add(num)
    return duplicados
#ejemplo15
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos_ordenados(conjunto):
    primos = {num for num in conjunto if es_primo(num)}
    return sorted(primos)
#ejemplo 17
def palabras_segun_longitud_ordenadas(conjunto_palabras, longitud):
    return {palabra for palabra in conjunto_palabras if len(palabra) == longitud and palabra == ''.join(sorted(palabra))}
#ejmplo 19
def numeros_ordenados_y_sin_duplicados(conjunto):
    numeros_ordenados = sorted(list(conjunto))
    return set(numeros_ordenados)

conjunto_de_numeros = {5, 3, 8, 2, 5, 8, 1, 2, 9, 4}
conjunto_ordenado_sin_duplicados = numeros_ordenados_y_sin_duplicados(conjunto_de_numeros)
print(conjunto_ordenado_sin_duplicados)