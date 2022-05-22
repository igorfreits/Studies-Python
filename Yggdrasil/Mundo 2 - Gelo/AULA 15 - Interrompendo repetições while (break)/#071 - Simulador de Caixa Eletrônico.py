print(f'{"Over Bank":-^40}')

valor = int(input('Qual valor você quer sacar? R$ '))

total = valor
cédula = 50
total_cedulas = 0
while True:
    if total >= cédula:
        total -= cédula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} de R$ {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cedulas = 0

        if total == 0:
            break

print(f'{"Volte sempre ao banco Over" :-^40}')
