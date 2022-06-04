from operator import index


lista = []
while True:
    number = int(input('Digite um valor: '))

    print(lista)
    if number not in lista:
        print(f'Voce adicionou \033[36m{number}\033[m a sua lista')
        lista.append(number)
    else:
        print(f'\033[35mVoce ja digitou esse numero!\033[m')
        lista.pop()

    option = input('Deseja continuar: [S/N]').upper().strip()

    if lista == lista:
        print()
    match  option:
        case 'S':
            continue
        case 'N':
            break
print(sorted(lista))
