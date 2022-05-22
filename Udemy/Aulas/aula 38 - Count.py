"""
Count - Contadores infinitos
"""

from itertools import count
from types import GeneratorType


variável1 = zip('Alo', 'Alo')
print(isinstance(variável1, GeneratorType))  # Verifica se é um gerador

variável2 = ((x, y)for x, y in zip('Alo', 'Alo'))
print(variável2)

# Count - Conta os valores
contador = count()
# Count(start=5, step=2)
print(next(contador))  # Exibi um valor
print(next(contador))
print(next(contador))

for valor in contador:  # Laço infinito por causado o contador
    if valor <= 5:
        print(valor)

lista = ['Igor', 'Michele', 'Noah']
lista = zip(contador, lista)
print(lista(lista))
