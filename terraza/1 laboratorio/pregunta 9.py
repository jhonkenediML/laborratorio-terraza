a=input("ingrese la letra")
b="aeiou"
j="".join(a.split())
c=j.lower()
contador=0
for carecter in c:
    if carecter in b:
        contador+=1
print (contador)