"""Asserções (Assertions)

-https://docs.python.org/pt-br/3/library/doctest.html
-https://docs.python.org/pt-br/3/library/unittest.html
"""
# Usar para outros desenvolvedores
# afirma que a função soma recebe dois parâmetros inteiros ou float


def soma(a, b):
    assert isinstance(a, (int, float)), 'A precisa ser int ou float'
    assert isinstance(b, (int, float)), 'B precisa ser int ou float'
    return a + b


if __name__ == '__main__':
    # soma(20, '20')  # AssertionError: A precisa ser int ou float

    # Tratamento de erro
    try:
        print(soma(20, '20'))
    except AssertionError as e:
        print(f'\033[31mConta invalida: {e}\033[m')
