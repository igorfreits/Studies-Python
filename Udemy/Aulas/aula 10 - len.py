"""
len - Quantidade de caracteres
"""

usuário = input('Digite seu Usuário: ')

# Conta Caracteres (obs: espaços contam/ so funcionam com str)
qtd_caracteres = len(usuário)
if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Cadastrado com sucesso')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

# soma dos lens
print(
    f'A quantidade de caracteres digitado foi: {len(string1) + len(string2)}')
print(string1.__len__())
print(string2.__len__())
