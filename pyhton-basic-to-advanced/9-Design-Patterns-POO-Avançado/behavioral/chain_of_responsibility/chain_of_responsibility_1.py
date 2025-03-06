# Implementando com funções


def handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'handler_ABC: Conseguiu tratar o valor {letter}'
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'handler_DEF: Conseguiu tratar o valor {letter}'
    return handler_unosolved(letter)


def handler_unosolved(letter: str) -> str:
    return f'handler_unosolved: Não conseguiu tratar o valor {letter}'


if __name__ == '__main__':
    print(handler_ABC('A'))
    print(handler_ABC('B'))

    print(handler_ABC('D'))

    print(handler_ABC('G'))
