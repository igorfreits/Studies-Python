"""aula-111-Unittest#1"""


def soma(x, y):
    """Soma x e y
    >>> soma(10, 20)
    30
    >>> soma(-10, 20)
    10
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(
        x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(
        y, (int, float)), 'y precisa ser int ou float'
    return x + y
