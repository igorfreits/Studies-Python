"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""
from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


class BoxStructure(ABC):  # Component
    @abstractmethod
    def print_contente(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):  # Composite
    def __init__(self, name) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_contente(self) -> None:
        print(f'\n\033[34m{self.name}:\033[0m')
        for child in self._children:
            child.print_contente()

    def get_price(self) -> float:
        return sum([
            child.get_price()for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):  # Leaf
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def print_contente(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # Leaf
    camiseta1 = Product('Camiseta', 49.90)
    camiseta2 = Product('Camiseta', 100.50)
    camiseta3 = Product('Camiseta', 99.90)

    # Composite
    caixa_de_camisetas = Box('Caixa de camisetas')
    caixa_de_camisetas.add(camiseta1)
    caixa_de_camisetas.add(camiseta2)
    caixa_de_camisetas.add(camiseta3)
    caixa_de_camisetas.print_contente()

    # Leaf
    smartphone1 = Product('Smartphone', 9100.00)
    smartphone2 = Product('Smartphone', 11100.00)

    # Composite
    caixa_smartphones = Box('Caixa de smartphones')
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)
    caixa_smartphones.print_contente()

    # composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_de_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_contente()

    print(caixa_grande.get_price())
