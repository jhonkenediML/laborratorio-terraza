def pares(n):
    if n<=100:
        if n%2==0:
            print(n)
        pares(n+1)
pares(1)