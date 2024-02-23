import numpy as np

def matriz_covarianza(matriz1, matriz2):
    try:
# Convertir las matrices a arrays de NumPy
        array1 = np.array(matriz1)
        array2 = np.array(matriz2)
#se Verificara que ambas matrices tengan la misma forma
        if array1.shape != array2.shape:
            raise ValueError("Las matrices deben tener la misma forma para calcular la covarianza.")

 # se Calcular la matriz de covarianza
        covarianza = np.cov(array1, array2, rowvar=False)

        return covarianza
    except ValueError as e:
#si es que 
        print(f"Error: {e}")
        return None

# Ejemplo de uso
matriz_a = np.random.rand(5, 3)  
# Matriz de ejemplo 1
matriz_b = np.random.rand(5, 3) 
# Matriz de ejemplo 2

matriz_de_covarianza = matriz_covarianza(matriz_a, matriz_b)

if matriz_de_covarianza is not None:
# si esque la matriz es matriz_de_covarianza se ejecutara
#por el contrario si es NOne no se ejecutara
    print("Matriz A:")
    print(matriz_a)

    print("\nMatriz B:")
    print(matriz_b)

    print("\nMatriz de Covarianza:")
    print(matriz_de_covarianza)