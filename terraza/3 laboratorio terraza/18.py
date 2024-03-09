#ejercicio 18 
def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    """
    Esta función recibe un conjunto de palabras y una letra,
    y devuelve un conjunto con las palabras que contienen esa letra, ordenadas de mayor a menor.
    """
    palabras_con_la_letra = {
        palabra for palabra in conjunto_palabras if letra in palabra
    }
    palabras_ordenadas = sorted(palabras_con_la_letra, key=len, reverse=True)
    return palabras_ordenadas

# Ejemplo de uso:
conjunto_palabras = {"manzana", "banana", "pera", "uva", "sandía", "melón"}
letra_buscada = "a"

resultado = palabras_con_letra_ordenadas(conjunto_palabras, letra_buscada)
print(f"Palabras con la letra '{letra_buscada}' ordenadas de mayor a menor: {resultado}")