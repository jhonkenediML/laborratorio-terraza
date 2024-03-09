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
# ejercicio 2
def palabras_con_letra(palabras, letra):
    """
    Esta función recibe un conjunto de palabras y una letra,
    y devuelve un conjunto con las palabras que comienzan con esa letra.
    """
    palabras_con_letra = set()

    for palabra in palabras:
        if palabra.startswith(letra):
            palabras_con_letra.add(palabra)

    return palabras_con_letra

# Ejemplo de uso:
conjunto_palabras = {"manzana", "banana", "pera", "uva", "sandía", "melón"}
letra_inicial = "m"

resultado = palabras_con_letra(conjunto_palabras, letra_inicial)
print(f"Palabras que comienzan con '{letra_inicial}': {resultado}")
# ejerccio 3
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
# ejercicio 4
def interseccion_entre_conjuntos(conjunto1, conjunto2):
    """
    Esta función recibe dos conjuntos de números
    y devuelve un conjunto con los números que están en ambos conjuntos.
    """
    interseccion = conjunto1.intersection(conjunto2)
    return interseccion

# Ejemplo de uso:
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado = interseccion_entre_conjuntos(conjunto_a, conjunto_b)
print(f"Intersección entre los conjuntos: {resultado}")
#ejercicio 5
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1 - conjunto2

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado_diferencia = diferencia_entre_conjuntos(conjunto_a, conjunto_b)

print(f"Diferencia entre {conjunto_a} y {conjunto_b}: {resultado_diferencia}")
#ejercicio 6
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    """
    Esta función recibe dos conjuntos de números
    y devuelve un conjunto con los números que están en el segundo conjunto pero no en el primero.
    """
    diferencia = conjunto2 - conjunto1
    return diferencia

# Ejemplo de uso:
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

resultado = diferencia_entre_conjuntos(conjunto_a, conjunto_b)
print(f"Diferencia entre los conjuntos: {resultado}")
#ejercicio 7
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
# ejercicio 8
def palabras_palindromas(conjunto_palabras):
    """
    Esta función recibe un conjunto de palabras
    y devuelve un conjunto con las palabras que son palíndromas.
    """
    palindromas = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    return palindromas

# Ejemplo de uso:
conjunto_palabras = {"radar", "oso", "python", "reconocer", "casa"}

resultado = palabras_palindromas(conjunto_palabras)
print(f"Palabras palíndromas: {resultado}")
#ejercicio 9
def longitud(n,e):
    l={palabra for palabra in e if len(palabra )==n}
    return l
s = {"casa", "perro", "gato", "sol", "luna", "auto"}
print(longitud(int(4),s))
#ejercicio 10
def palabras(cnpalabras,letra):
    b={palabra for palabra in cnpalabras if letra in palabra}
    return b
s = {"manzana", "banana", "pera", "uva", "sandía", "melón"}    
print(palabras(s,"a"))
#ejercicio 11
def numero(conjunto):
    b=sorted(list(conjunto))
    return b
s = {5, 3, 8, 2, 1, 9, 4}
print(numero(s))
#ejercicio 12
def numeros_ordenados_descendente(conjunto_numeros):
    """
    Esta función recibe un conjunto de números
    y devuelve un conjunto con los números ordenados de mayor a menor.
    """
    numeros_ordenados = set(sorted(conjunto_numeros, reverse=True))
    return numeros_ordenados

# Ejemplo de uso:
s = {5, 2, 8, 1, 9, 3}
print(numeros_ordenados_descendente(s))
#ejercicio 13
def numeros_duplicados(conjunto):
    duplicados = set()
    for num in conjunto:
        if list(conjunto).count(num) > 1:
            duplicados.add(num)
    return duplicados


# ejercicio 14
def numeros_no_duplicados(conjunto_numeros):
    """
    Esta función recibe un conjunto de números
    y devuelve un conjunto con los números que no están duplicados.
    """
    numeros_no_duplicados = {numero for numero in conjunto_numeros if list(conjunto_numeros).count(numero) == 1}
    return numeros_no_duplicados

# Ejemplo de uso:
conjunto_numeros = {5, 2, 8, 1, 9, 3, 5, 2, 8}

resultado = numeros_no_duplicados(conjunto_numeros)
print(f"Números no duplicados: {resultado}")
# ejercicio 15
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
# ejercicio 16
def palabras_palindromas_ordenadas(conjunto_palabras):
    """
    Esta función recibe un conjunto de palabras
    y devuelve un conjunto con las palabras palíndromas ordenadas de menor a mayor.
    """
    palindromas_ordenadas = sorted(
        {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    )
    return palindromas_ordenadas

# Ejemplo de uso:
conjunto_palabras = {"radar", "oso", "python", "reconocer", "casa"}

resultado = palabras_palindromas_ordenadas(conjunto_palabras)
print(f"Palíndromos ordenados: {resultado}")
# ejercicio 17
def palabras_segun_longitud_ordenadas(conjunto_palabras, longitud):
    return {palabra for palabra in conjunto_palabras if len(palabra) == longitud and palabra == ''.join(sorted(palabra))}
#ejercicio 18 
def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    """
    Esta función recibe un conjunto de palabras y una letra,
    y devuelve un conjunto con las palabras que contienen esa letra, ordenadas de mayor a menor.
    """
    palabras_con_la_letra = {
        palabra for palabra in conjunto_palabras if letra in palabra
    }
    palabras_ordenadas = sorted(palabras_con_la_letra, key=len, reverse=True)
    return palabras_ordenadas

# Ejemplo de uso:
conjunto_palabras = {"manzana", "banana", "pera", "uva", "sandía", "melón"}
letra_buscada = "a"

resultado = palabras_con_letra_ordenadas(conjunto_palabras, letra_buscada)
print(f"Palabras con la letra '{letra_buscada}' ordenadas de mayor a menor: {resultado}")
#ejercicio 20
def palabras_palindromas_longitud(conjunto_palabras, longitud):
    """
    Esta función recibe un conjunto de palabras, una longitud determinada,
    y devuelve un conjunto con las palabras palíndromas que tienen esa longitud, ordenadas de menor a mayor.
    """
    palindromas_filtradas = {
        palabra for palabra in conjunto_palabras
        if palabra == palabra[::-1] and len(palabra) == longitud
    }
    palindromas_ordenadas = sorted(palindromas_filtradas)
    return palindromas_ordenadas

# Ejemplo de uso:
conjunto_palabras = {"radar", "oso", "python", "reconocer", "casa"}
longitud_deseada = 3

resultado = palabras_palindromas_longitud(conjunto_palabras, longitud_deseada)
print(f"Palíndromos de longitud {longitud_deseada} ordenados: {resultado}")