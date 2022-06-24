"""
Groupby - Agrupando valores
"""
from itertools import groupby, tee

# Agrupar elementos dentro de  um dicionario
# groupby necessita que esteja na ordem(Notas)
# tee - Faz copia do iterador

alunos = [
    {'nome': 'Igor', 'nota': 'A'},
    {'nome': 'Noah', 'nota': 'B'},
    {'nome': 'Michele', 'nota': 'A'},
    {'nome': 'Israel', 'nota': 'C'},
    {'nome': 'Alice', 'nota': 'D'},
    {'nome': 'Annie', 'nota': 'A'},
    {'nome': 'Leona', 'nota': 'B'},
    {'nome': 'Karma', 'nota': 'A'},
    {'nome': 'Lulu', 'nota': 'C'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'A'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'A'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'B'},
    {'nome': 'Peter', 'nota': 'A'},
]

for aluno in alunos:
    print(aluno)


def ordena(item):
    return item['nota']


alunos.sort(key=ordena)  # organizou com base nas notas
alunos_agrupados = groupby(alunos, ordena)

# Extrai a chave para agrupamento
# Com tee
for agrupamento, valores_agrupados in alunos_agrupados:
    val1, va2 = tee(valores_agrupados)

    print(f'agrupamento: {agrupamento}')

    for aluno in val1:
        print(f'\t aluno')

    quantidade = len(list(val1))
    print(f'\t{quantidade} alunos e tiraram a nota: {agrupamento}')
    print()

'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''
