list = []
for i in range(0, 5):
    value = int(input('digite um valor: '))
    if i == 0 or value > list[-1]:
        list.append(value)
        print('Adicionado ao final da lista')
    else:
        position = 0
        while position < len(list):
            if i <= list[position]:
                list.insert(position, i)
                print(f'Adicionado na posição {position}')
                break
            position += 1
print(f'Valores digitados {list}')
