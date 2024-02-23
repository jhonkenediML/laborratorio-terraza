def factorial(numero):
    if numero <0: 
        return False
    elif numero==0 or numero==1:
        numero=1
    else:
        n=1
        for i in range(2, numero+1):
            n*= i
        
        return n
a=int(input("ingrese un numero"))
b=factorial(a)
print(f"el fatorila de{a}\nes  {b} ")

