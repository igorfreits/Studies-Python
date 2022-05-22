"""
Levantando exceções(raise)
"""
# https://docs.python.org/3/library/exceptions.html


def divide(n1,  n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)  # Retorna o valor None
        raise  # Relança a exceção


try:  # Não sera executado se nao tiver o raise porque o erro ja foi tratado
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)


def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')  # Criação de uma exceção
    return n1 / n2


try:
    print(divide2(2, 0))
except ValueError as error:
    print('Você está tentando dividir por 0')
    print('Log: ', error)
