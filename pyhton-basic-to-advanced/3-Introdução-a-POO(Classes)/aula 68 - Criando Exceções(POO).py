"""Criando Exceções(POO)"""


class ItsWrongError(Exception):  # it's wrong - Esta errado
    # Exceções devem terminar com Error
    pass


def test():
    raise ItsWrongError('Error!')


try:
    test()
except ItsWrongError as error:
    print(f'Erro:{error}')
