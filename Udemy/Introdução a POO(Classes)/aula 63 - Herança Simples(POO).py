"""Herança Simples(POO)"""

# Relação
"""
Herda os atributos da Super classe/classe pai e defini seus próprios atributos

# A classe caneta escreve e a sua herança lapiseira também escreve, mas também pode escreve em gravite

A herança é um princípio próprio à programação orientada a objetos (POO)
que permite criar uma nova classe a partir de uma já existente.
Herança, também chamada de subclasses, provém da subclasse,
da classe recém-criada que contém atributos e métodos da qual deriva.
A principal vantagem da herança é a capacidade para definir novos atributos e
métodos para a subclasse, que se somam aos atributos e métodos herdados.
"""

"""
Associação - Usa
Agregação - Tem
Composição - é dono
Herança - é
"""


class People:  # Super classe/Classe pai
    def __init__(self, name, year):
        self.name = name
        self.year = year
        # Pega o nome da classe que esta sendo usada no momento
        self.name_class = self.__class__.__name__

    def speak(self):  # Falar
        # Client e Student irão herdar também
        print(f'{self.name_class} Falando')  # Exibi qual classe esta falando


class Client(People):  # Subclasses/classe filho
    def purchase(self):  # Comprar
        print(f'{self.name_class} comprando')
# Mantém os atributos da super classe(People) e tem os seus próprios atributos


class Student(People):  # Subclasses/classe filho
    def studying(self):  # Estudar
        print(f'{self.name_class} estudando')
# Mantém os atributos da super classe(People) e tem os seus próprios atributos


c1 = Client('Igor', 23)
print(c1.name)  # Herdou os atributos de People
c1.speak()  # Client falando/Herança da classe People
c1.purchase()

a1 = Student('Alice', 14)

a1.speak()  # Student falando/Herança da classe People
a1.studying()

p1 = People('Isra', 14)
p1.speak()
