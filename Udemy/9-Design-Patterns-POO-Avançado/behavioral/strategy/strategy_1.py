"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle) -SOLYD
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Order:  # Context
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discont = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discont(self):
        return self._discont.calculate(self._total)


class DiscountStrategy(ABC):  # Strategy
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercentDiscount(DiscountStrategy):  # Strategy A
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercentDiscount(DiscountStrategy):  # Strategy B
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):  # Strategy C
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):  # Strategy D
    def __init__(self, discount: float):
        self._discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self._discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercentDiscount()
    fifty_percent = FiftyPercentDiscount()
    no_discount = NoDiscount()
    custom_discount = CustomDiscount(10)

    order = Order(1000, twenty_percent)
    print(order.total, order.total_with_discont)

    order = Order(1000, fifty_percent)
    print(order.total, order.total_with_discont)

    order = Order(1000, no_discount)
    print(order.total, order.total_with_discont)

    order = Order(1000, custom_discount)
    print(order.total, order.total_with_discont)
