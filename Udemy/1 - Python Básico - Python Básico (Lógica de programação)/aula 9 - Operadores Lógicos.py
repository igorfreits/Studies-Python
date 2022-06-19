"""
operadores lógicos
and, or, not
in e not in
"""

# and - E
# (Verdadeiro E verdadeiro) = True
# (falso E verdadeiro) = False

a = 2
b = 2
c = 3

print(a == b and b < c)

# or - OU
# verdadeiro OU verdadeiro = True

# not - INVERSOR
n1 = 2
n2 = 3
if not n2 > n1:
    print('B é maior do que A')
else:
    print('A é maior que B')

a1 = ''
a2 = 0
if not a1:
    print('Por favor, preencha o valor de a2')

# in - EM
nome = 'Igor'
if 'I' in nome:
    print('Exite a letra I no seu nome')
else:
    ('Não existe a letra no seu nome')

# not in - Inverte
nomme = 'Michele'
if 'M' not in nome:
    print('Execute')
else:
    print('Existe o texto')

usuário = input('Qual o usuário: ')
senha = input('Senha do usuário: ')
usuario_bd = 'Igor'
senha_bd = '12345'

if usuario_bd == usuário and senha_bd == senha:
    print('Você esta logado no sistema')
else:
    print('Senha ou usuário incorreto')
