"""Sobreposição de membros(POO)"""

"""Quando eu falo em sobreposição de método eu estou falando simplesmente que eu quero.
Sobrescrever/reescrever algum método"""

"""Pode reescrever o construtor(__init__) isso quer dizer que se o construtor for definido abaixo da classe pai
estaria sobrepondo o construtor da calasse pai e teria que escrever tudo de novo"""


class People:  # Super classe/Classe pai
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.name_class = self.__class__.__name__

    def speak(self):  # Falar
        print(f'{self.name_class} Falando')


class Client(People):  # Subclasses/classe filho
    def purchase(self):  # Comprar
        print(f'{self.name_class} comprando')

    def speak(self):
        print('Estou em cliente')


class Student(People):  # Subclasses/classe filho
    def studying(self):  # Estudar
        print(f'{self.name_class} estudando')

# Sobreposição


class ClientVIP(Client):  # Herda atributos do Client que herda de People
    def __init__(self, name, year, last_name):  # sobreposição
        super().__init__(name, year)  # chama o construtor sua classe pai
        self.last_name = last_name  # Sobrenome

    def speak(self):  # sobreposição do método speak

        # super().speak() - Busca na cadeia a classe speak de suas classes pai

        People.speak(self)  # chama o speak da classe escolhida
        Client.speak(self)
        print(f'{self.name} {self.last_name}')


c2 = ClientVIP('Michele', 25, 'Almeida')
c2.speak()  # Chama um método da classe People, mesmo sendo herança da classe Client
