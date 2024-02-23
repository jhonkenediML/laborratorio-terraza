import numpy as np
def medi(matriz):
    try:
        b=np.array(matriz)
        mediana=np.median(b)
        media=np.mean(b)
        estadar=np.std(b)
        return f"la media{media}y la mediana{mediana} el estadar es {estadar}"
    except ValueError:
        print("no es numeo")
        return None

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(medi(a))
