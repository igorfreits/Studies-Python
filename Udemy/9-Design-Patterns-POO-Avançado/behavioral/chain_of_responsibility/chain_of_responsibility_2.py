"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    3

    def __init__(self):
        self.sucessor = Handler

    @abstractmethod
    def handler(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['A', 'B', 'C', ]
        self.sucessor = sucessor

    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f'"{letter}" is a letter of the HandlerABC'
        return self.sucessor.handler(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['D', 'E', 'F', ]
        self.sucessor = sucessor

    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f'"{letter}" is a letter of the HandlerDEF'
        return self.sucessor.handler(letter)


class HandlerUnsolved(Handler):
    def handler(self, letter: str) -> str:
        return f'HandlerUnsolved: "{letter}" is not a letter of the ABC or DEF'


if __name__ == '__main__':
    handler_unosolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unosolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handler('A'))
    print(handler_abc.handler('B'))

    print(handler_abc.handler('D'))
    print(handler_def.handler('C'))

    print(handler_abc.handler('G'))
    print(handler_def.handler('H'))
