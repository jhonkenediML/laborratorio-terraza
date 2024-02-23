import numpy as np
import random
# se intala al ordenador la blioteca numpy para utilizarlo.

import numpy as np
def maximo(matriz):
    try:
        a=np.array(matriz)
        maximo=np.max(matriz)
        return maximo
    except ValueError:
        print("noes numero")
        return None
b=[[1,2,3],[4,5,6],[7,8,9]]
print(maximo(b))
