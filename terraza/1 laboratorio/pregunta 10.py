A=int(input("ingrese asta que numero desea que se realise "))
fibonacci = [0, 1]
for i in range(2, A):
    siguiente_numero = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(siguiente_numero)
print("Los primeros ",A,"números de la serie Fibonacci son:")
print(fibonacci)

