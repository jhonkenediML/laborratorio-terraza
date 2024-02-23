def imprimir_piramide(n, fila=1):
    if fila <= n:
        for i in range(1, fila + 1):
            print(i, end=" ")
        print()
        imprimir_piramide(n, fila + 1)

# Ejemplo de uso
imprimir_piramide(5)

