# Tuplas são imutáveis
# Tuplas contem ( )

lanche = ('Hambúrguer', 'Suco', 'Pudim', 'Pizza', 'Batata frita')
print(type(lanche))  # Tupla

print(lanche[1])  # Suco

print(lanche[-2])  # Pudim

print(lanche[1:3])  # Mostra suco e pudim (Fatiamento)

print(len(lanche))  # Mostra a quantidade de itens na tupla

# lanche[1] = 'Refrigerante'

# Mensagem de erro quando se tenta alterar um a tupla
# TypeError: 'tuple' object does not support item assignment

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba!')

print()

for cont in range(0, len(lanche)):
    print(f'Hoje eu vou comer {lanche[cont]}')

print()

for pos, c in enumerate(lanche):
    print(f'Vou comer {c} na posição {pos}')
