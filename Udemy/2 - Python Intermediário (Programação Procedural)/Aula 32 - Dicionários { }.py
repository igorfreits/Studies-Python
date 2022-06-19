"""
Dicionários{}
"""
# Dicionários são similares a lista e podem conter indices
# No Dicionários você controla de índice (chave)
# Dicionários sao {} compostas de chaves e valores
# Pode adicionar = "strings", "int", "float"
# Dicionários = {"Key" : "Valor"}

d1 = {'chave1': 'valor  da chave'}
d1['nova_chave'] = 'Valor da nova chave'  # Adiocona um valor ao Dicionários

print(type(d1))
print(d1)
print(d1['chave1'])  # Escolhe a posição do Dicionário

# Cria um dicionario
d2 = dict(chave1='Valor da chave', chave='Valor da outra chave1')
print(d2)

# Sera exibido o ultimo valor da chave 1
d3 = {1: 'chave,', 1: 'chave 2', 1: 'chave real'}
print(d3)  # chaves devem ser únicas, e cadauma deve conter o seu valor

# Valores que podem ser usados como chave
d4 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 0): 'Tupla',
}
print(d4[123])

d4['naoexiste1'] = 'Agora Existe'

if 'naoexiste1' in d4:
    print(d4['naoexiste1'])

# Retorna None, pois não existe essa chave no dicionario
print(d4.get('naoexiste2'))

d4.update({'chave_nova': 'novo_valor'})  # Adiocona um novo item ao dicionario
print('chave_nova')

del d4['str']  # Apaga um valor do dicionario

print(123 in d4)  # Retorna o valor True
print('Outro valor' in d4.values())  # Checa se a chave existe
print((1, 2, 3, 0) in d4.keys())  # Checa se exite a key

print(len(d4))  # Mostra o numero quantos pares existem

for c, d in d4.items():  # Iteraval
    print(c)
    #print(c[0], c[1])
    print(c, d)

# Dicionario dentro de dicionários
clientes = {
    'cliente1': {
        'nome': 'Igor',
        'sobrenome': 'Freitas',
    },
    'cliente2': {
        'nome': 'Michele',
        'sobrenome': 'Almeida',
    },
}

for clientes_k, client_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in client_v.items():
        print(f'\t{dados_k} = {dados_v}')


dd = {1: 'a', 2: 'b',  3:  'c', 'd': ['Igor', 'Freitas']}
v = dd
print(v)
print(dd)

v[1] = 'Igor'  # Ambos mostram, os mesmos resultados
print(v)
print(dd)

v = dd.copy()  # Cria uma copia
v[1] = 'Melancia'
print(dd)
print(v)

v['d'][0] = 'Joãozinho'  # Acessa  a lista dentro dicionario
print(dd)
print(v)

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

tupla = (
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
)

dd1 = dict(lista)  # converte uma lista em um dicionario
print(dd1)

dd2 = dict(tupla)  # converte uma tupla em um dicionario
print(dd2)

dd3 = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
}
dd3.pop(4)  # elimina um item especifico
print(dd3)
dd3.popitem()  # elimina o  ultimo item
print(dd3)

dd4 = {
    'a': 'b',
    'c': 'd',
}
dd3.update(dd4)  # Concatenação dos dicionários
print(dd3)

emails_gerentes = {
    'Iguatemi': 'iguatemi@gmail.com',
    'Plaza': 'plaza@hotmail.com',
    'Barra': 'barra@gamil.com',
}
print(emails_gerentes['Barra'])
email = emails_gerentes['Iguatemi']
print(email)

# Se o valor ou ja existir ele irar substituir
# Adiciona um novo item
emails_gerentes['Leblon'] = 'leblon@gmail.com'
#                 chave          valor
print(emails_gerentes)

# Para cada "item no meu dicionário"
for shopping in emails_gerentes:  # Iterável
    print(shopping)

print(emails_gerentes.keys())  # Exibi as chaves do dicionário


for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print(email)

print(emails_gerentes.values())  # Exibi os valores das chaves

emails_gerentes.pop('Leblon')  # remove a chave escolhida
print(emails_gerentes)

# Verifica se um Shopping Existe
if 'Iguatemi' in emails_gerentes:
    print('Existe')
else:
    print('Nao existe')
