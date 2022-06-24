"""
Módulos padrão
Módulos são arquivos .py(Que contem código python) e servem para expandir
as funcionalidades padrão da linguagem

https://docs.python.org/pt-br/3/py-modindex.html
"""
from sys import platform as so  # Apelida o mudulo
from random import randint, random
from random import *  # '*'Importa todo o modulo random

print(so)  # Mostra qual sistema esta sendo utilizado


def randint(*args):  # Esta sobrescrevendo o modulo randint
    return 'hahahahah'


for i in range(10):
    print(randint(0, 10))

for i in range(10):
    # gera um numero aleatorio entre a e 1 com ponto flutuante
    print(randint(0, 10), random())
