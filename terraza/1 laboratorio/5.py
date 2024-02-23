def primos(numero):
    if numero < 2:
        return "no es un numero par els jun rreal"
    elif numero%2==0:
        return "no es primo"
    else:
        return"es primo"
a=int(input("ingrese un numero"))
b=primos(a)
print(f"el numero\n{a} \n es {b}")