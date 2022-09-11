"""Callable"""

from collections.abc import Callable

SomaInteiros = Callable[[int, int], int]


def executa(func: SomaInteiros, a: int, b: int) -> int:
    return func(a, b)


def soma1(a: int, b: int) -> int:
    return a + b


def soma2(a: float, b: str) -> dict[str, float]:
    return a + b


executa(soma2, 1, 2)
