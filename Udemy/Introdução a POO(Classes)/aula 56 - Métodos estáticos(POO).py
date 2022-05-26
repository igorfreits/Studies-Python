"""
Métodos estáticos
"""
# staticmethod  - não necessita da classe em si e da instancia(decorador)
# Um método estático não recebe um primeiro argumento implícito

from random import randint


class Pessoa:
    ano_atual = 2022  # Atributo de classe e esta disponível para todas as instancias

    def __init__(self, nome, idade):
        # Estão relacionados a instancia(self) e precisam receber uma instancia
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        # A variável so esta disponível dentro da função
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


print(Pessoa.gera_id())
