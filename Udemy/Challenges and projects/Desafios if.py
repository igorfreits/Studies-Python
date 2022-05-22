"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n1 = input('Digite uma numero: ')

if n1.isdigit():
    n1 = int(n1)

    n2 = n1 % 2
    if n2 == 0:
        print(f'{n1} é Par')
    else:
        print(f'{n1} é Impar')
else:
    print('Por favor Digite um numero')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hr = input('Digite um horario 0 a 23: ')

if hr.isdigit():
    hr = int(hr)
    if hr < 0 or hr > 23:
        print('Horario deve estar entre 0 e 23')
    if hr <= 11:
        print('Bom dia')
    elif hr > 18:
        print('Boa noite')
    else:
        print('Boa tarde')
else:
    print('Digite um horario entre 0 a 23')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

usuário = input('Digite um numero de usuário: ')
tamanho = len(usuário)

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome esta OK')
else:
    print('Seu nome é muito grande')
