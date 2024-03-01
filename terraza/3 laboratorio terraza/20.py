#ejercicio 20
def palabras_palindromas_longitud(conjunto_palabras, longitud):
    """
    Esta función recibe un conjunto de palabras, una longitud determinada,
    y devuelve un conjunto con las palabras palíndromas que tienen esa longitud, ordenadas de menor a mayor.
    """
    palindromas_filtradas = {
        palabra for palabra in conjunto_palabras
        if palabra == palabra[::-1] and len(palabra) == longitud
    }
    palindromas_ordenadas = sorted(palindromas_filtradas)
    return palindromas_ordenadas

# Ejemplo de uso:
conjunto_palabras = {"radar", "oso", "python", "reconocer", "casa"}
longitud_deseada = 3

resultado = palabras_palindromas_longitud(conjunto_palabras, longitud_deseada)
print(f"Palíndromos de longitud {longitud_deseada} ordenados: {resultado}")