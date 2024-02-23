numero= int(input("Ingrese un número: "))

if numero<= 1:
    primo = False
else:
    primo = True
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

if primo:
    print("El número",numero,"primo")
else:
    print("El número ",numero,"no es primo.")