def factorial(numero):
    if numero<0:
        return "no esta definido el factorial"
    elif numero ==0 or numero == 1:
        return 1
    else:
        resultado=1
        for i in range (2, numero+1):
            resultado*=i
        return resultado
B=int(input("ingrese el numero"))
A=factorial(B)
print("el factorial de ",B, "es:",A)