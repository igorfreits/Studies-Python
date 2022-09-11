"""Tipos opcionais (Optional Typing)"""


def soma(x: int, y: float | None = None) -> float:
    return x + y


soma(1, 0)
soma(1, None)
