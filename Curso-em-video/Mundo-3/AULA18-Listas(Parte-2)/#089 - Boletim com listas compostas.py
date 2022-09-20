ficha = list()

while True:
    nome = input('Nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])

    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}\033[35m{a[2]:>8.1f}\033[m')

while True:
    print('-='*35)
    option = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if option == 999:
        print('FINALIZANDO...')
        break

    if option <= len(ficha) - 1:
        print(f'As notas de \033[34m{ficha[option][0]}\033[m são \033[34m{ficha[option][1]}\033[m')
