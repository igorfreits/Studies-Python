c = 0
list = []
while True:
    value = int(input('enter a value :'))
    list.append(value)
    option = str(input('Continue? [Y/N]')).upper().strip()
    if option == 'Y':
        c += 1
        continue
    elif option == 'N':
        break
    else:
        print('invalid option')
print(f'Voce digitou {c} elementos')
print(
    f'Os valores da lista em ordem decrescente sao {sorted(list,reverse=True)}')
if 5 not in list:
    print('O valor 5 nao esta presente na lista')
else:
    print(f'O valor esta presente na lista na posição {list.index(5)}')
