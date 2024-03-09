# ejercicio 2
def palabras_con_letra(palabras, letra):
    """
    Esta función recibe un conjunto de palabras y una letra,
    y devuelve un conjunto con las palabras que comienzan con esa letra.
    """
    palabras_con_letra = set()

    for palabra in palabras:
        if palabra.startswith(letra):
            palabras_con_letra.add(palabra)

    return palabras_con_letra

# Ejemplo de uso:
conjunto_palabras = {"manzana", "banana", "pera", "uva", "sandía", "melón"}
letra_inicial = "m"

resultado = palabras_con_letra(conjunto_palabras, letra_inicial)
print(f"Palabras que comienzan con '{letra_inicial}': {resultado}")