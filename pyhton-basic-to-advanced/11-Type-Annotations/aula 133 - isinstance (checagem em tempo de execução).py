"""isinstance (checagem em tempo de execução)"""


def soma(x: int, y: float | None = None) -> float:
    if isinstance(y, float | int):
        return x+y
    return x+x


print(soma(3, 20))
print(soma(50, 1.5))
