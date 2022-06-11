""" Composição(POO)"""

"""A classe endereço pertence à classe cliente
Quando a classe cliente é criada e cria uma classe endereço assim
que ela for apagada a classe endereço que foi usada por ela
também será apagada da memória.

Isso se chama composição relação de composição"""

# Relação de composição
"""Composição, uma classe usa, depende e mantém uma referencia da outra classe
(se a classe principal morre, as filhas também morrem)"""

"""Se a classe principal for apagada todos os objetos
que a classe principal utilizou vão ser apagados com ela"""


class Client:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.addresses = []  # Endereços

    def insert_address(self, city, state):  # cidade e estado
        self.addresses.append(Address(city, state))

    def list_address(self):
        for address in self.addresses:
            print(address.city, address.state)

    def __del__(self):
        print(f'{self.name} FOI APAGADO')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city}/{self.state} FOI APAGADO')


client1 = Client('Igor', 23)
client1.insert_address('Portugal', 'PT')
print(client1.name)
client1.list_address()
del client1

print()

client2 = Client('Michele', 21)
client2.insert_address('São Paulo', 'SP')
client2.insert_address('Rio de Janeiro', 'RJ')
print(client2.name)
client2.list_address()
del client2

print()

client3 = Client('Noah', 15)
client3.insert_address('Belo Horizonte', 'MG')
print(client3.name)
client3.list_address()
del client3

print('#'*100)
