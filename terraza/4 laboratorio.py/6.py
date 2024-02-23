 # 6 Asegurar que un ciclo while se ejecuta al menos una vez
contador=0
while contador < 10:
    contador+=1
    assert contador == 10,"el contador no se repite"
