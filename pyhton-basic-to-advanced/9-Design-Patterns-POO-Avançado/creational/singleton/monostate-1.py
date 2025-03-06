"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


from typing import Dict


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state: Dict = {
        'x': 10,
        'y': 20
    }  # Estado inicial do objeto

    def __init__(self, nome=None, sobrenome=None):
        self.x = 100000  # Não afeta o valor do estado inicial
        self.__dict__ = self._state
        #  self.x = 100000 - Mudou o valor depois que foi convertido o estado interno calasse
        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome


# class A(StringReprMixin):
#     def __init__(self, nome):
#         self.x = 20
#         self.y = 10
#         self.nome = nome


# a = A('Igor')
# print(a.__dict__)
# print(a)
if __name__ == '__main__':
    m1 = MonoStateSimple('Igor')
    m2 = MonoStateSimple(sobrenome='Freitas')
    m1.x = 100
    # Podemos ver que o m2 não foi alterado porque o estado é igual para todas as instâncias

    print(m1)
    print(m2)
