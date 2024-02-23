import numpy as np
# se utiliza la biblioteca numpy para 
#utilizar matricez
def media_matriz(matriz):
#se cra la funcionn que tomara de entrada matricez
    try:
        matriz= np.array(matriz)
        media = np.mean(matriz)
        return media
#si es verda se ejecutara las intrucciones
    except ValueError:
        print("La matriz debe contener solo números.")
        return None
#cuando no cumple con los parametroz devolvera el error
# Ejemplo de uso
matriz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

media = media_matriz(matriz_a)

if media is not None:
    print("Matriz:")
    print(np.array(matriz_a))

    print(f"\nMedia de los elementos de la matriz: {media}")