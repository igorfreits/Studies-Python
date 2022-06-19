"""
Descompactamento de listas em python
"""

lista = ['Igor', 'João', 'Robert', 1, 2, 3, 4, 5, 6, 7,
         8, 9, 100]
# * RESTO DE VALOR - cria uma nova lista
# n1,n2 = lista (Erro de valores, pois não tem toda a lista nas variáveis)

n1, n2, n3, *outra_lista, ultimo_valor = lista

print(n2, outra_lista)  # exibe n2 e uma nova lista ligada a variável
print(ultimo_valor)  # exibe o ultimo valor da lista

*outra_lista, n1, n2, n3 = lista
print(n1, n2,)  # Exibi o penúltimo e ultimo valor

# *_ é uma variável ,mas significa que nao serão usados certos valores da lista
n1, n2, *_ = lista
print(n1, n2)
