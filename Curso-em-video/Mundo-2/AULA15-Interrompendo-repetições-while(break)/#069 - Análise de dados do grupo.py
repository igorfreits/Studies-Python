print('-'*30)
print('Cadastro de pessoas')
print('-'*30)

idade18 = totalm = totalf20 = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]: ')).upper()[0].strip()

    idade = int(input('Qual a idade? '))

    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        totalm += 1
    if sexo == 'F' and idade < 20:
        totalf20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Relatório de cadastro:'
      f'\n Ao total tivemos {idade18} pessoas maiores de 18 anos'
      f'\n Tivemos {totalm} homens cadastrados'
      f'\n E um total de {totalf20} mulheres com menos de 20 anos')
print('Acabou')
