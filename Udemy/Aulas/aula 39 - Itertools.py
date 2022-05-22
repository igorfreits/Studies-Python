"""
Combinations, Permutations e Product -Itertools

Combinação - Ordem nao importa
permutação - Ordem importa
ambos nao repetem valores únicos
produto - Ordem importa e repete valores únicos
"""
# Importar biblioteca Itertools
# Valores iteraveis

from itertools import combinations, permutations, product
pessoas = ['Igor', 'Michele', 'Noah', 'Alice', 'Israel', 'Colomk']

# Obtém todos as combinações possíveis dentro da lista em grupos de 2
# 'Igor', 'Michele' - Não ira retornar o inverso
for grupo in combinations(pessoas, 2):
    print(grupo)

print()

# 'Igor', 'Michele' - retornar o inverso
for grupo in permutations(pessoas, 2):
    print(grupo)

print()

# Retorna valores iguais
for grupo in product(pessoas, repeat=2):  # Quantas vezes ira repetir
    print(grupo)
