'''Formatar  String
f ou .format()'''

nome = 'Igor'
idade = 23
altura = 1.75
peso = 70
imc = peso / (altura * altura)


# :2.f = mostra um float com duas casas decimais
print(f'{nome} tem {idade} anos de idade e tem um IMC de: {imc:.2f}')
print('{}, tem {} anos de idade e seu IMC é de:{}'.format(nome, idade, imc))
print('{n}, tem {i} anos de idade e seu IMC é de:{im}'.format(
    n=nome, i=idade, im=imc))
print('{0}, tem {1} anos de idade e seu IMC é de:{2}'.format(nome, idade, imc))
