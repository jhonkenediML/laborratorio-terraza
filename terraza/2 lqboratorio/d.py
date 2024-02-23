9
def elemento_central(matriz): 
# la funcion toma como entrada una matriz
    filas, columnas = len(matriz), len(matriz[0])

    if filas % 2 == 1 and columnas % 2 == 1:
 #si las filas son impares devuelve  
        centro = (filas // 2, columnas // 2)
 #se calcula las cordenadas
        elemento_central = matriz[centro[0]][centro[1]]
 #se calcula el numero de filas y columnas
        return elemento_central
    else:
        return None  
#si las matrices son pares devuelve
matriz_ejemplo = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
# se presenta una matriz de ejemplo
# para observar la ejecucion de la funcion
elemento_central = elemento_central(matriz_ejemplo)

if elemento_central is not None:
#se evaluara si es elemento_central pero si none no se ejecutara
    print("Matriz:")
    for fila in matriz_ejemplo:
#cuando la fila esta en la matrz
        print(fila)
#se imprimra la fila en la pantalla
    print(f"\nElemento Central: {elemento_central}")
else:
#pero si no es nose inprimira
    print("La matriz no tiene un único elemento central porque su tamaño es par.")
10
import numpy as np
# se intala al ordenador la blioteca numpy para utilizarlo.

def suma_matrices(matriz1, matriz2):
#se tomara como entrada dos matricez
    try:
        resultado = np.array(matriz1) + np.array(matriz2)
#se intenta sumar las matrices utilizando NumPy y se corta en np
        return resultado.tolist()
    
    except ValueError:
#se evaluara si esque son matricez diferentess
        print("No se pueden sumar matrices de diferentes tamaños.")
        return None
#deulve para que informe que nose podra realizar la suma

# Ejemplo de uso
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

resultado_suma = suma_matrices(a, b)

if resultado_suma is not None:
#si l amatriz es numeros se realizara pero si noes se dara None
    print("Matriz A:")
    print(np.array(a))
# se imprimem la primera
    print("\nMatriz B:")
    print(np.array(b))
# se imprimem la segunda
    print("\nResultado de la suma:")
# se imprime la suma de las dos matrices
    print(np.array(resultado_suma))
    11
def multiplicar(matriz, numero):
#la funcion  tomara matriz y sera multiplicado por un numero
    resultado = [[elemento * numero for elemento in fila] for fila in matriz]
 # se muestra una exprexion de lista anidada  
    return resultado

# Ejemplo de uso
matriz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escalar = 2

resultado = multiplicar(matriz_a, escalar)

print("Matriz original:")
for fila in matriz_a:
    print(fila)
#se imprimira si la fila esta en la matriz
print(f"\nResultado de multiplicar la matriz por {escalar}:")
for fila in resultado:
    print(fila)
# se imprimira el resultado
12
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
#la  funcion se almacena en "a"
a = media_matriz(matriz_a)

if a is not None:
# si es a se imprimira quiere decir si tiene valor 
#por el contrario si es que no hay datos o variables nose ejecutara
    print("Matriz:")
    print(np.array(matriz_a))
#se imprimera la matriz con vertida en array
    print(f"\nMedia de los elementos de la matriz: {a}")
13
import numpy as np
import random
#se impreme las dos bibliotecas para ejecutar los codigo 
matriz_aleatoria = np.random.rand(100, 100)
# Crear una matriz de números aleatorios de tamaño 100x100
print(matriz_aleatoria)
# Imprimir la matriz aleatoria
14
import numpy as np
# se intala al ordenador la blioteca 
#numpy para utilizarlo.
def estadisticas_matriz(matriz):
#Se define la función 
#estadisticas_matriz que toma una matriz como entrada
    try:
#se evaluara todo en cada uno de las indicaciones
        matriz_np = np.array(matriz)
#se cobierte la matriz dada a un array
        media = np.mean(matriz_np)
        mediana = np.median(matriz_np)
#calculan las do media  mediana su media de la matriz
        desviacion_estandar = np.std(matriz_np)
        return media, mediana, desviacion_estandar
#se ejecuta sin errores, se devuelve una tupla con las estadísticas calculadas.   
    except ValueError:
#si esque no tiene como entrada numeros este le reponera
        print("La matriz debe contener solo números.")
        return None
# se Creara una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)
# Calcular estadísticas
resultados = estadisticas_matriz(matriz_aleatoria)
if resultados is not None:
#si es que tiene u valor o alguna varia el resultado se ejecutara
#pero si nohay valor es none y nose ejecutara
    print("Matriz Aleatoria:")
    print(matriz_aleatoria)
# se imprime la matriz_aleatoria
    media, mediana, desviacion_estandar = resultados
# se almacena toda estos codigos en resultado
    #lugo solo se imprime se muestra en ala pantalla
    print("\nEstadísticas:")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviación Estándar: {desviacion_estandar}")
15
import numpy as np
import random
# se intala al ordenador la blioteca numpy para utilizarlo.

def encontrar_elemento_maximo(matriz):
    try:
# si son valores numericos se ejecutara y se calularael amximo valor
        matriz_np = np.array(matriz)
        maximo = np.max(matriz_np)
        return maximo
    except ValueError:
#si noes es un valor numerico  
        print("La matriz debe contener solo números.")
        return None

# Ejemplo de uso
matriz_ejemplo = np.random.randint(1, 100, size=(3, 4))  
# Crear una matriz de ejemplo

maximo = encontrar_elemento_maximo(matriz_ejemplo)

if maximo is not None:
# se ejecutara si es maximo
# pero si es none nose ejecutara
    print("Matriz:")
    print(matriz_ejemplo)

    print(f"\nElemento Máximo: {maximo}")
16
import numpy as np
# se utiliza la biblioteca numpy
def submatriz_mayor_suma(matriz):
# la funcion sera una matriz
    matriz_np = np.array(matriz)
    #se comvierte en array
    filas,columnas = matriz_np.shape
    #la fila y la columna seran matriz_np.shape
    mejor_suma = float('-inf')
    mejor_submatriz = None
#se genera algunos parametros para que se ejecute la matriz
    for i in range(filas):
        for j in range(columnas):
            for k in range(i, filas):
                for l in range(j, columnas):
                    suma_actual = np.sum(matriz_np[i:k+1, j:l+1])
                    if suma_actual > mejor_suma:
                        mejor_suma = suma_actual
                        mejor_submatriz = matriz_np[i:k+1, j:l+1]

    return mejor_submatriz.tolist()

# Ejemplo de uso
matriz_ejemplo = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]
# se ejecutara toda las funciones 
resultado = submatriz_mayor_suma(matriz_ejemplo)
print("Submatriz de mayor suma:")
#se mostrara toda los resultados en la pntalla
print(resultado)
17
import numpy as np
# se utiliza la biblioteca numpy para 
#utilizar matricez
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
    # se imprime la matriz_a en la pantalla
    print("\nMatriz B:")
    print(matriz_b)
    # se imprime la matriz_b en la pantalla

    print("\nMatriz de Covarianza:")
    print(matriz_de_covarianza)
    #se imprime la funcion matriz_de_covarianza