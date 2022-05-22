# IMPORTAÇÕES
import json
from math import pi
import dadosone

"""
Aula 41, 42,43
"""

produtos = [
    {'nome': 'p1', 'preço': 13},
    {'nome': 'p2', 'preço': 55.55},
    {'nome': 'p3', 'preço': 5.59},
    {'nome': 'p4', 'preço': 22},
    {'nome': 'p5', 'preço': 81.23},
    {'nome': 'p6', 'preço': 5.7},
    {'nome': 'p7', 'preço': 10.90},
    {'nome': 'p8', 'preço': 89.82},
    {'nome': 'p9', 'preço': 12},
    {'nome': 'p10', 'preço': 2.90},

]

pessoas = [
    {'nome': 'Igor', 'idade': 23},
    {'nome': 'Colomk', 'idade': 21},
    {'nome': 'Michele', 'idade': 20},
    {'nome': 'Noah', 'idade': 5},
    {'nome': 'Alice', 'idade': 15},
    {'nome': 'Israel', 'idade': 27},
    {'nome': 'Lukas', 'idade': 55},
    {'nome': 'Gabriela', 'idade': 58},
    {'nome': 'Felipe', 'idade': 19},
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
aula 48.1 e 48.1
"""

PI = pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


if __name__ == '__main__':
    lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(pi)
    print(__name__)

"""
aula 49
"""


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return dadosone.real(r)
    else:
        return r


def redução(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    if formata:
        return dadosone.real(r)
    else:
        return r


d1 = {
    'Pessoa 1': {
        'nome': 'Igor',
        'idade': 23,
    },
    'Pessoa 2': {
        'nome': 'Michele',
        'idade': 21,
    },
}
d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
