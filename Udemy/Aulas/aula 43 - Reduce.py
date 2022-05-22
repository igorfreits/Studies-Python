"""
Reduce
"""
# Precisa importar biblioteca
# Acumuladora de valores

from dados import pessoas, produtos, lista
from functools import reduce

# Acumulador com for
c = 0
for item in lista:
    c += item

print(c)
# Função(), acumulador, item: item + acumulador, lista, inicio do acumulador
soma_lista = reduce(lambda ac, i: i + ac,  lista, 0)
print(soma_lista)
#                               chave do dicionario
soma_preços = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(soma_preços)  # Soma de todos valores
print(soma_preços / len(produtos))  # Media do produtos

soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idade)  # Soma das idades
print(soma_idade / len(pessoas))  # Media das idades
