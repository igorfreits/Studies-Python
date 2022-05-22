"""
Geradores, Iteradores e Iteráveis
"""

import time
import sys
l1 = [0, 1, 2, 3, 4, 5]
print(hasattr(l1, '__iter__'))  # Verifica se o objeto é iterável

l1 = iter(l1)
print(hasattr(l1, '__next__'))  # Verifica se o objeto é um iterador

print(next(l1))  # Retorna um valor de cada vez
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))

for v in l1:  # Iterador - exibi cada valor  em uma linha
    print(v)

l2 = list(range(1000))
# Exibi quanto de memoria esta consumindo no computador
print(sys.getsizeof(l2))

"""Cria [] em branco e faz uma interação na função range pegando de
0 a 99 e coloca esses valores a cada iteração do laço ela coloca um dos valores no meu no meu [] vazio
"""


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
print(g)
for v in g:  # avaliação preguiçosa - retorna um valor de cada vez
    print(v)

"""
A palavra-chave yield é uma instrução Python usada para definir as funções geradoras em Python.
A instrução yield só pode ser usada dentro do corpo da função.
A principal diferença entre uma função geradora e uma função regular é
que a função geradora contém uma expressão yield em vez da instrução return
"""


def gera1():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel


g1 = gera1()
print(next(g1))
print(next(g1))
print(next(g1))

l1 = [x for x in range(100)]  # Lista
print(type(l1))

l2 = (x for x in range(100))  # Gerador
print(type(l2))

print(sys.getsizeof(l1))  # Armazena valore e salva na memoria
print(sys.getsizeof(l2))  # So entrega o valor quando for pedido

