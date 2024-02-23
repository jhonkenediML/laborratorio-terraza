def palabras_segun_longitud_ordenadas(conjunto_palabras, longitud):
    return {palabra for palabra in conjunto_palabras if len(palabra) == longitud and palabra == ''.join(sorted(palabra))}
