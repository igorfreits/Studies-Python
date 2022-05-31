class Client:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.adresses = []  # Endereços

    def insert_address(self, city, state):  # cidade e estado
        self.adresses.append(Address(city, state))

    def list_address(self):
        for address in self.adresses:
            print(address.city, address.state)

    def __del__(self):
        print(f'{self.name} FOI APAGADO')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city}/{self.state} FOI APAGADO')


"""A classe endereço pertence à classe cliente
Quando a classe cliente é criada e cria uma classe endereço assim
que ela for apagada a classe endereço que foi usada por ela
também será apagada da memória.

Isso se chama composição relação de composição"""
