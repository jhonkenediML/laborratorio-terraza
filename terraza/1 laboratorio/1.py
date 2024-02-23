"""Realiza la suma, resta, multiplicación
 y división de dos números ingresados por 
   usuario."""
p,s=int(input("ingrese un numero  ")),int(input("ingrese el segundo numero"))
a,b,c=p+s,p-s,p*s

if s!=0:
    d=p/s
else:
    print("no es posible la divición")
print(f'la suma es  {a}\n la resta  {b}\nla multiplicacion  {c}la divicion{d}')