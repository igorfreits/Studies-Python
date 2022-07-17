"""Listas compostas"""


# Criação de uma lista composta
teste = list()
teste.append('Igor')
teste.append(23)
galera1 = list()
galera1.append(teste[:])  # Adicionando uma lista dentro de outra lista
print(galera1)
# Deve colocar o [:] para quebrar o linkamento entre as listas

teste[0] = 'João'  # Alterando o valor da lista
teste[1] = 25
galera1.append(teste[:])
print(galera1)

galera2 = [
    ['Michele', 19], ['Alice', 25],
    ['Noah', 23], ['Israel', 21]
]
print(galera2[0])  # ['Michele', 19]
print(galera2[1][0])  # Alice
print(galera2[3][1])  # 21

for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera3 = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera3.append(dados[:])
    dados.clear()  # Limpando a lista para não criar varios dados
print(galera3)

total_maior = total_menor = 0
for p in galera3:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor += 1
print(f'Temos {total_maior} maiores e {total_menor} menores de idade')
