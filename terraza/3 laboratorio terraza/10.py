def palabras(cnpalabras,letra):
    b={palabra for palabra in cnpalabras if letra in palabra}
    return b
s = {"manzana", "banana", "pera", "uva", "sandía", "melón"}    
print(palabras(s,"a"))