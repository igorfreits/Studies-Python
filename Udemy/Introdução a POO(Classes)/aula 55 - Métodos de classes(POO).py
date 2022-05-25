"""
Métodos de classes
"""
# métodos de classe são métodos que são relativos à classe inteira
# Método de instancia - Precisam precisam de umas instancia (self)
# Classmethod - Precisa da classe em si

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
        # A variável so esta disponível dentro daa função
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa('Igor', 23)
p1.get_ano_nascimento()

p1 = Pessoa.por_ano_nascimento('Igor', 1999)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
