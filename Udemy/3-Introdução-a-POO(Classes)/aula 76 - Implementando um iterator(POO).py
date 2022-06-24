"""Implementando um iterator"""


class MyList():  # Recriação de  uma lista
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, value):  # Adiciona itens
        self.__items.append(value)

    def __getitem__(self, index):  # Exibi valor selecionado
        return self.__items[index]

    def __setitem__(self, index, value):  # Muda valores da lista
        if index >= len(self.__items):
            self.__items.append(value)
        self.__items[index] = value

    def __delitem__(self, index):  # Apaga um item especifico da lista
        del self.__items[index]

    def __iter__(self):  # itera
        return self

    def __next__(self):  # Proximo item da lista
        try:  # Exceção para caso cair em algum erro
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):  # Mostra a lista(print)
        return f'{self.__class__.__name__}{(self.__items)}'


if __name__ == '__main__':
    lista = MyList()
    lista.add('Igor')
    lista.add('Michele')

    print(lista)

    for value in lista:
        print(value)

# print(next(list))
print(lista[0])
lista[0] = 'Alice'
print(lista)

lista = list(lista)  # Converte para uma lista normal do pythom

for value in lista:
    print(value)
