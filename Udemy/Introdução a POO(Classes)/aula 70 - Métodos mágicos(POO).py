"""Métodos mágicos(POO)"""

"""https://rszalski.github.io/magicmethods/"""

# Dunder: métodos que começam e terminam com dois _ (métodos mágicos)
# Modificam o comportamento da classe


class A:
    def __new__(cls, *args, **kwargs):  # Construtor

        if not hasattr(cls, '_already_exists'):  # Ja existe
            cls. _already_exists = object.__new__(cls)  # Cria copia
        return cls._already_exists

        # (É executado antes do __init__)
        cls.name = 'Igor'  # Atributo de classe

        def haha(*args, **kwargs):
            print('Fala  oi')
        cls.haha = haha

        return object().__new__(cls)  # Toda classe deriva de object

    def __init__(self):  # Construtor
        # Executado quando a classe é instanciada
        print('Eu sou o INIT')

# Call - Faz a classe funcionar como função e continua sendo uma classe
# -Precisa ser chamado como uma função
    def __call__(self, *args, **kwargs):

        print(args)
        print(kwargs)

        result = 1
        for i in args:
            result *= i
        return result

# Quando for configurar um atributo novo na sua classe ele vai ser chamado
    def __setattr__(self, key, value):
        if key == 'name':  # Caso alguém defina uma chave com o nome "name"
            self.__dict__[key] = 'Voce nao pode fazer isso'
        else:
            self.__dict__[key] = value

    def __del__(self):  # não é garantido que seja chamado
        print('Objeto coletado')

    def __str__(self):
        # Modifica o que aparece quando uma instancia é chamada num print
        return "<class 'A'>"

    def __len__(self):
        return 55


a = A()
print(len(a))
print(a)
a.name = 'Igor'
a.cheese = 'Queijo'
print(a.name, a.cheese)


b = A()
c = A()
print(a == b)
print(id(a), id(b), id(c))  # Mesma referencia

a(1, 2, 3, 4, 5, name='Igor')
# Retorna uma tupla com os números e um dic de name

variable = a(1, 2, 3, 4, 5)
print(variable)
