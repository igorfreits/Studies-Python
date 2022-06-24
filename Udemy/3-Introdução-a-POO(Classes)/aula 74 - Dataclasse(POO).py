"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.

Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
# dataclasses são classes normais, mas ela também é um  code generator
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


@dataclass(eq=True, repr=True, frozen=False, init=True)
# eq - comparação
# frozen - Deixa a class imutável
# repr - representação imprimível do objeto
# init - Inicializador
# order - Permite a organização de itens
class People:
    name: str
    last_name: str = field(repr=False)  # Sobrenome

    def __post_init__(self):  # método que é executado apos o init
        if not isinstance(self.name, str):
            raise TypeError(
                f'invalide Type {type(self.name).__name__} != str em {self}')

    @property
    def full_name(self):  # nome completo
        return f'{self.name} {self.last_name}'


p1 = People('Igor', 'Freitas')
p2 = People('Igor', 'Freitas')
p3 = People('100', '2')

print(p1 == p2)  # eq


peoples = [p1, p2, p3]
print(sorted(peoples, key=lambda people: people.last_name, reverse=True))

print(p1.name)
print(p1.last_name)
print(p1.full_name)

print(asdict(p1))  # dict
print(astuple(p2))  # tuple
