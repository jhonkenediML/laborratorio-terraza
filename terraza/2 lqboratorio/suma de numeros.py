def suma_hasta_n(n, acumulador=0):
    if n > 0:
        acumulador += n
        suma_hasta_n(n - 1, acumulador)
    else:
        print(f"La suma de los números del 1 al {n} es: {acumulador}")

# Ejemplo de uso
suma_hasta_n(5)
