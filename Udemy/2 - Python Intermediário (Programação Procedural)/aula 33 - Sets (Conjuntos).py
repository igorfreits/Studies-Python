"""
SETS (Conjuntos)
add(adiciona), update(atualiza), clear, discard
union | (une)
intersection & (Todos o elementos presentes nos dois sets)
diference - (Elementos apenas no set da esquerda)
    symmetric_difference ^(Elementos que estão nos dois sets, mas nao em ambos)
"""

# Sets são semelhantes a listas[], Dicionários{} e tuplas()
# So suportam elementos unicos
# Não possui indices
# Semelhante ao dicionario, mas sem as chaves

s1 = {1, 2, 3, 4, 5}  # set
print(type(s1))

a = {}  # Cria um dicionario ao invés de um set
b = set()  # Set vazio

b.add(1)  # Adiciona um item ao set
b.add(2)
b.add(3)
print(b)

b.discard(2)  # Descarta um valor do set
print(b)

for v in s1:  # Iterável
    print(v)

s2 = set()
# .update() - Adiciona um item ao set e itera sobre o valor
# (A iteração nao segue um padrão)
s2.update('python')
print(s2)

s3 = set()
# set não aceitam elementos duplicados
s3.update([1, 2, 4, 5, 6, ], {5, 6, 7, 8})
print(s3)

l1 = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 7, 8, 9, 'Igor', 'Igor']
l1 = set(l1)  # Converte lista para set e remove os valores duplicados
print(l1)
# converte set para lista, e voltam sem as duplicadas,
# mas podem aparecer fora de ordem
l1 = list(l1)
print(l1)

s4 = {1, 2, 3, 4, 5}
s5 = {1, 2, 3, 4, 5, 6}
ss = s4 | s5  # Une os valores do set(union | )
print(ss)

ss = s4 & s5  # Mostra somenos o elementos duplicados(intersection & )
print(ss)

# Mostra o elemento do set da esquerda <,
# mas nao pode estar presente nos dois(difference - )
ss = s5 - s4
print(ss)

l2 = ['Igor', 'Michele', 'Noah']
l3 = ['Igor', 'Michele', 'Noah', 'Noah', 'Noah']

# Muda a lista para set
l2 = set(l2)
l3 = set(l3)
print(l2, l3)
print(l2 == l3)

if set(l2) == set(l3):
    print('L2 é igual a L3')
else:
    print('L2 é diferente de L3')
