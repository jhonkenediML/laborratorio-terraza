
A = int(input("ingrese el numero que desea inicio: "))
B = int(input("ingrese el numero que desea final: "))
i = 0
for numero in range(A, B + 1):
    if numero % 2 == 0:
        i += numero
print("La suma de los números pares en el rango de",A," a",B,"  es: ",i)
