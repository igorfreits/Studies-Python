"""Atributos de Classe (POO)"""


class A:
    vc = 123  # Variável da classe
    # Disponível para todas as instancia da classe

    def __init__(self):
        # self.vc = 321 Variável de instance
        pass


a1 = A()
a2 = A()

a1.vc = 321  # Criação de atributo direto na instancia


print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print()

A.vc = 'Alterado'

print(a1.vc)
print(a2.vc)
print(A.vc)
