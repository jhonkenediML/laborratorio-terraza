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
