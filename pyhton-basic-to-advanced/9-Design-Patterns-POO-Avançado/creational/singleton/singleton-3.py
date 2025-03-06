# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('Call é executado antes de instanciar')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass = Meta):
#     def __new__(cls, *args, **kwargs):
#         print('New é chamado antes do __init__')

#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('Init é chamado depois do __new__')
#         self.nome=nome

#     def __call__(self, x, y):
#         print('call', self.nome, x+y)


# p1=Pessoa('Igor')
# print(p1.nome)
from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Tema escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema claro'

    as2 = AppSettings()
    as2.tema = 'Tema vermelho'

    as3 = AppSettings()
    
    print(as3.tema)
    print(as1 == as2)
    print(as1 is as3)
    print(as2 == as3)
