"""Doctests

-https://docs.python.org/pt-br/3/library/doctest.html
"""

# Adiciona testes na documentação(docstring)


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


def subtrai(x, y):
    """Subtrai x e y
    >>> subtrai(10, 5)
    5
    >>> subtrai('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
    """
    assert isinstance(
        x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(
        y, (int, float)), 'y precisa ser int ou float'
    return x - y


if __name__ == '__main__':
    import doctest

    # Caso a documentação esteja errada o doctest irá mostrar o erro
    doctest.testmod(verbose=True)  # Exibirá detalhes dos testes
