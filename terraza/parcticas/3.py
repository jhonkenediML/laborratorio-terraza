def piramide (n,fila=1):
    if fila <=n:
        for i in range (1,fila+1):
            print(i,end=" ")
        print()
        piramide(n,fila+1)
piramide(5)
