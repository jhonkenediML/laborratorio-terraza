# ejercicio 8
def palabras_palindromas(conjunto_palabras):
    """
    Esta función recibe un conjunto de palabras
    y devuelve un conjunto con las palabras que son palíndromas.
    """
    palindromas = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    return palindromas

# Ejemplo de uso:
conjunto_palabras = {"radar", "oso", "python", "reconocer", "casa"}

resultado = palabras_palindromas(conjunto_palabras)
print(f"Palabras palíndromas: {resultado}")