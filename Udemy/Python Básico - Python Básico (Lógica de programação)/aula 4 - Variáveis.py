"""Variáveis

= Atribuição
#iniciar com letra, pode conter numeros, separar com _, letras minusculas"""

nome = 'Igor'
idade = 23
altura = 1.75
e_maior = idade > 18
peso = 70
imc = peso / (altura * altura)
ano = 2022

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É de maior:', e_maior)
print(nome , 'tem', idade, 'anos de idade e seu imc é de: ', imc)

print('{} tem {} anos de idade e pesa {} kg'.format(nome, idade, peso))
print('{} tem um IMC de {:.2f}'.format(nome, imc))
print('{} nasceu no ano de: {}'.format(nome, ano - idade))