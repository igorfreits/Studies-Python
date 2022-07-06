from datetime import date
contador = 1
menor = 0
maior = 0

for c in range(7):
    ano = int(input(f'Em que ano nasceu a {contador}ª pessoa? '))
    contador += 1
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos um total de {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menor de idade')
