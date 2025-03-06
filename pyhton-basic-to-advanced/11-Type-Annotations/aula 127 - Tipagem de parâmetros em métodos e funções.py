"""Tipagem de parâmetros em métodos e funções"""

# x e y devem ser inteiros
# z deve ser um número de ponto flutuante
# obs.: float aceita tanto int como float,
# int aceita apenas int.
# Para informar o retorno da função, use:
# `-> tipo` antes dos dois pontos, como em
# def () -> None: para funções sem retorno


def soma(x: int, y: int, z: float) -> float:
    return x + y + z


print(soma('a', 2, 3))
# Argument 1 to "soma" has incompatible type "str"; expected "int"


lista_inteiros: list[int] = [1, 2, 3, 4, 5]
lista_strings: list[str] = ['a', 'b', 'c', 'd', 'e']
lista_tuplas: list[tuple] = [(1, 'a'), (2, 'b')]
lista_lista_int: list[list[int]] = [[1], [4, 5]]
