"""
Listas -[]
"""

lanche = ['hambúrguer', 'suco', 'pizza', 'pudim']  # [0, 1 , 2 , 3]'
print(lanche[3])

# Comandos da lista
lanche.append('Picole')  # .append() -Adiciona um item no final da lista
# .insert() - Adiciona um item na posição selecionada
lanche.insert(0, 'Coxinha')
del lanche[3]  # del - Apaga o item selecionado
lanche.pop(2)  # .pop - Remove o ultimo item da lista ou pode usar o parametro
# lanche.remove('Pizza')  # .remove - Remove um valor da lista


if ' Chocolate' in lanche:
    lanche.remove('Chocolate')  # Remove 'Chocolate' se estiver na lista

valores = list(range(4, 11))  # Conta de 4 ate 10
print(valores)

v1 = [8, 2, 4, 8, 3, 0]
valores.sort()  # .sort - Organiza os valores da lista
valores.sort(reverse=True)  # Organiza na ordem reversa
len(v1)  # Conta  os item da lista

if 10 in v1:
    v1.reverse(10)
else:
    print('Fim')

v2 = list()
v2.append(4)
v2.append(10)
v2.append(15)

for c, v in enumerate(v2):
    print(f'Na posição encontrei {c} encontrei o valor...{v}')

a = [2, 3, 4, 6]
b = a
b[2] = 0  # Lista igualada com a
print(f'Lita A: {a}')
print(f'Lista B: {b}')

print()

c = [2, 3, 4, 6]
d = c[:]  # Cria uma copia dos valores de c
c[2] = 0
print(f'Lita C: {c}')
print(f'Lista D: {d}')
