"""
Dicionários
São estruturas compostas por chave e valor
{chave:valor}
"""

pessoas = {'nome': 'Igor', 'sexo': 'M', 'idade': 23}  # Dicionário
print(pessoas['nome'])  # Acessando o valor da chave 'nome'

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())  # Mostra as chaves
print(pessoas.values())  # Mostra os valores
print(pessoas.items())  # Mostra as chaves e os valores

for k in pessoas.keys():  # Mostra as chaves
    print(k)

for v in pessoas.values():  # Mostra os valores
    print(v)

for k, v in pessoas.items():  # Mostra as chaves e os valores
    print(f'{k} = {v}')

del pessoas['sexo']  # Deleta a chave 'sexo'
print(pessoas)

pessoas['nome'] = 'Alice'  # Altera o valor da chave 'nome'
print(pessoas)

pessoas['peso'] = 60.3  # Adiciona uma nova chave e valor
print(pessoas)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1])  # Mostra o dicionário
print(brasil[0]['uf'])  # Mostra o valor da chave 'uf' do dicionário 0

estado = dict()  # Cria um dicionário vazio
brasil = list()  # Cria uma lista vazia

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()
    brasil.append(estado.copy())  # Copia o dicionário para a lista

for e in brasil:
    for k, v in e.items():
        print(f'O campo \033[34m{k}\033[m tem valor \033[34m{v}\033[m')
