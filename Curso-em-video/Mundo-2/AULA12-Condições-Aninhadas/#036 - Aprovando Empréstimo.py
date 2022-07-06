casa = float(input('Qual o valor da casa? R$: '))
salario = float(input('Quanto é o seu salario?R$: '))
anos = int(input('Quantos anos de financiamento?: '))

prestacao = casa / (anos * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos'
      f'\n a pretação sera de {prestacao:.2f}')

minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Empretimo aprovado!')
else:
    print('Empretimo Negado!')
