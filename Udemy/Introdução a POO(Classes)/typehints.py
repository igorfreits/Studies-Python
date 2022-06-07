# Aula 73
from typing import Union
"""Document of this models
Ele não faz nada, mas é um exemplo pra você

-Typing: https://docs.python.org/pt-br/3/library/typing.html
"""
x: int = 10
y: float = 10.5
z: bool = False


def function1(p1: float, p2: str, p3: dict) -> float:
    return 1.50


function1(1.5, 'str', {})


def function2() -> Union[list, dict]:
    return []
