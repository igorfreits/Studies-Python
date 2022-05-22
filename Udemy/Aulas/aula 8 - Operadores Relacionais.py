"""
Operadores Relacionais
==, >, >=, <, <=, !=
"""

# Retorna um valor bool True/False

# == igualdade
print(2 == 2)

n1 = 2  # int
n2 = "2"  # string
print(n1 == n2)

# > maior que
num_1 = 15
num_2 = 4
print(num_1 > num_2)

# >= maior que ou igual ha
num1 = 69
num2 = 13
print(num1 >= num2)

# < menor que
nn1 = 3
nn2 = 465
print(nn1 < nn2)

# <= menor que ou igual ha
num__1 = 23
num__2 = 34
print(num__1 <= num__2)

# != Diferente
nome = 'Igor'
sobrenome = 'Freitas'
print(nome != sobrenome)

usuário = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade_menor = 20  # muito jovem
idade_maior = 30  # muito velho
idade = int(idade)

if idade >= idade_menor and idade <= idade_maior:
    print(f'{usuário} pode pegar o empréstimo')
else:
    print(f'{usuário} não pode pegar o empréstimo')
