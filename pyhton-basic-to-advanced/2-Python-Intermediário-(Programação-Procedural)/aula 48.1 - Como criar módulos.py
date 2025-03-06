"""
Como criar módulos

https://docs.python.org/pt-br/3/tutorial/modules.html
"""
from math import pi

PI = pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= 1
    return r


lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(dobra_lista(lista))
print(multiplica(lista))
print(pi)
