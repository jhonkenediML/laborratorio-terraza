A= int(input("Ingrese un número para generar su tabla de multiplicar: "))
print("Tabla de multiplicar del número", A, ":")
for i in range(1, 11):
    resultado = A*i 
    print(A, "x", i, "=", resultado)