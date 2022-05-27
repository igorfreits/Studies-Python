"""@property - Getters e Setters(POO)"""
# Getter(=) - Obtém um valor - Funciona sozinho
# Setter(.) - Configura um valor


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
        self.name = name
        # So serve pra salvar o valor que ira usar no setter e getter

    @property  # Vira um atributo
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        print('Setter foi executado')
        self._name = name

    @property
    def surname(self):
        return 'DESCONHECIDO'


# Nunca chame um getter dentro de um getter ou setter dentro de um setter
"""_ Sustenta o valor e o que é uma função que obtém o valor do atributo que
tem um _.
O setter é uma função que configura o valor do atributo que tem um _"""

p1 = People('Alice')
# p1.name = 'Alice'
# print(p1._name)
print(p1.name)
print(p1.surname)
