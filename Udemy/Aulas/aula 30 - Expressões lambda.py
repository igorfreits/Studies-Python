"""
Expressões lambda - (funções anônimas)
"""


import re


def funcao(argumento1, argumento2):
    return argumento1 * argumento2


variavel = funcao(2, 2)
print(variavel)


# a = lambda x, y: x * y  # Não precisa de ()


# print(a(2, 2))

lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8],
]
# Lista dentro de lista


def funcao2(item):  # Para pegar a lista com o def
    return item[1]


lista.sort(key=funcao2)  # sort() Altera e organiza minha lista

print(lista)

# Para pegar a lista com lambda
lista.sort(key=lambda item: item[1])  # Não foi preciso criar um função
print(lista)

# sorted() - organiza minha lista, mas nao altera ela
print(sorted(lista, key=lambda i: i[1]))
print(sorted(lista, key=lambda i: i[1], reverse=True)) #reverse=True - Organiza em ordem reversa
