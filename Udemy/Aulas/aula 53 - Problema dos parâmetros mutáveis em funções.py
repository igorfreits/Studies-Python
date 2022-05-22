"""
Problema dos parâmetros mutáveis em funções
"""
# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None


def lista_de_clientes(clientes_iterável, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iterável)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
