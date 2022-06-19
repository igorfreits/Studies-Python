"""
Operador ternário em Python
"""

logged_user = True

if logged_user:  # A variável consta como True porque recebe um valor bool
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'
print(msg)

# Operador ternário

msg = 'User Logged' if (logged_user) else 'User_Error'
print(msg)

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    a = 'Pode acessar' if (e_de_maior) else 'Não pode acessar'
    print(a)

if idade >= 18:
    print('Pode acessar')
else:
    print('Não pode acessar')
