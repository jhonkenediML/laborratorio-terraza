numeros = input("Ingrese una lista de números separados por espacios: ")
lista_numeros = [int(numero) for numero in numeros.split()]
menor_a_mayor = sorted(lista_numeros)
print("Lista de números ordenados de menor a mayor:",menor_a_mayor)