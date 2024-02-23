def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def anagramas_en_conjunto(conjunto_palabras):
    anagramas = set()

    for palabra1 in conjunto_palabras:
        for palabra2 in conjunto_palabras:
            if palabra1 != palabra2 and son_anagramas(palabra1, palabra2):
                anagramas.add(palabra1)
                anagramas.add(palabra2)

    return anagramas

conjunto_de_palabras = {"roma", "amor", "perro", "roper", "casa", "saca"}
conjunto_de_anagramas = anagramas_en_conjunto(conjunto_de_palabras)
print(conjunto_de_anagramas)