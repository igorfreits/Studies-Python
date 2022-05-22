from datetime import date

ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print(f'O atleta tem {idade} anos ')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')  # ACIMA DE 25 ANOS