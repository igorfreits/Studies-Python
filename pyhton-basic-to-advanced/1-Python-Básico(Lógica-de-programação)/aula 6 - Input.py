'''Entrada de dados'''
# input() Recebe um valor

nome = input('Qual o seu nome? ')  # sempre retorna um str
idade = input('Qual a sua idade? ')
ano_nascimento = 2022 - int(idade)
print()  # print vazio pula uma linha

print('{} tem {} anos e nasceu no ano de {}'.format(nome, idade, ano_nascimento))

print()

n1 = int(input('Digite um numero: '))
n2 = input('Digite outro numero: ')
n2 = int(n2)

print(n1 + n2)
