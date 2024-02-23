def primos(numero):
    if numero<2:
        return False
    for i in range (2,numero+1):
        if numero%2==0:
            return numero
    return numero

def conjunto(conjuntos):
    cona=set()
    for numero in conjuntos:
        if primos (numero):
            cona.add(numero)
    return cona

b={1,2,3,4,5,6,7,8,9}

print(conjunto(b))