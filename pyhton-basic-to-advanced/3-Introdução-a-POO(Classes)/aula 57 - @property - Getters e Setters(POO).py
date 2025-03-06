"""@property - Getters e Setters(POO)"""
# Getter(.) - Obtém um valor - Funciona sozinho
# Setter(=) - Configura um valor


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        self.price = self.price - (self.price*(percentage/100))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.title()

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):  # Checa se o valor é uma instancia de str
            value = float(value.replace('R$', ''))
        self._price = value


p1 = Product('SHIRT', 'R$50')
p1.discount(10)
print(p1.name, p1.price)

p2 = Product('MUG', 15)
p2.discount(10)
print(p2.name, p2.price)

# Reforço


class People:
    def __init__(self, name):
        self._name = name

    @property  # pode existir sozinho
    def name(self):
        return self._name

    @name.setter  # Tem que pegar o método que foi usado no getter
    def name(self, name):  # Name = valor(argumento)
        self._name = name

    @property
    def sobrenome(self):
        return 'Desconhecido'


# Nunca chame um getter dentro de um getter ou setter dentro de um setter
"""_ Sustenta o valor
GETTER é uma função que obtém(get)o valor do atributo que
tem um _.
SETTER é uma função que configura o valor do atributo que tem um _"""

p1 = People('Noah')
# p1.name = 'Alice'
print(p1.name)
print(p1.sobrenome)
