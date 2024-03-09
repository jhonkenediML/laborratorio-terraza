from collections import deque

def es_palindroma(palabra: str) -> bool:
    """
    Determina si una palabra es palíndroma o no utilizando una cola.

    :param palabra: La palabra a verificar.
    :return: True si la palabra es palíndroma, False en caso contrario.
    """
    cola = deque(palabra)
    while len(cola) > 1:
        if cola.popleft() != cola.pop():
            return False
    return True