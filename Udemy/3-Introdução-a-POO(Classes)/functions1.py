# Aula 73
"""..."""


def sum(x, y):
    """Sum x and y"""
    return x+y


def multiplies(x, y, z=None):
    """multiplies x,y,z
    Devops pode omitir a variável z cao nao tenha necessidade de usar

    """
    if z:
        return x * y
    else:
        return x * y * z
