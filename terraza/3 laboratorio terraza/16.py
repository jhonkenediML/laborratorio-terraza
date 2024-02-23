def palabras_palindromas_ordenadas(conjunto_palabras):
    """
    Esta función recibe un conjunto de palabras
    y devuelve un conjunto con las palabras palíndromas ordenadas de menor a mayor.
    """
    palindromas_ordenadas = sorted(
        {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    )
    return palindromas_ordenadas

# Ejemplo de uso:
conjunto_palabras = {"radar", "oso", "python", "reconocer", "casa"}

resultado = palabras_palindromas_ordenadas(conjunto_palabras)
print(f"Palíndromos ordenados: {resultado}")