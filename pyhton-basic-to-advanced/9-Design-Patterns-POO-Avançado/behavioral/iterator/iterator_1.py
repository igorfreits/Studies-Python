"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):  # Concrete Iterator
    def __init__(self, collections: List[Any]) -> None:
        self.collections = collections
        self._index = 0

    def __next__(self):
        try:
            item = self.collections[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):  # Concrete Iterator
    def __init__(self, collections: List[Any]) -> None:
        self.collections = collections
        self._index = -1

    def __next__(self):
        try:
            item = self.collections[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):  # Concrete Aggregate
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Igor')
    mylist.add('Michele')
    mylist.add('Alice')
    # print(mylist)

    print('I stole a value: ', next(iter(mylist)))

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)
