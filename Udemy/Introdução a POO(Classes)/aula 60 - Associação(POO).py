"""Associação(POO)"""

# Relação de associação
"""Se relaciona com outra classe ou seja vai estar associada a outra classe.
Mas nenhuma das duas classes dependem uma da outra.
Ambas as classes podem viver uma sem a outra."""

"""Na associação uma classe "usa" código de outra classe,
mas não depende inteiramente disso para funcionar"""


class Writer:  # Escritor
    def __init__(self, name):
        self.__name = name
        self.__tool = None  # Ferramenta

    @property
    def name(self):
        # Não é possível acessar um atributo privado fora da classe
        # Pra acessar o atributo privada é preciso criar um getter
        return self.__name

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool):
        self.__tool = tool


class Pen:  # Caneta
    def __init__(self, brand):  # Marca
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def write(self):  # Escrever
        print('Caneta esta escrevendo...')


class TypeWriter:  # máquina de escrever
    def write(self):  # Escrever
        print('Maquina esta escrevendo...')


escritor = Writer('Isra')
caneta = Pen('Bic')
maquina = TypeWriter


print(escritor.name)
print(caneta.brand)
maquina.write(maquina)

escritor.tool = maquina
escritor.tool.write(maquina)
# Tool esta recebendo o objeto da classe inteira
# Associação entre o escritor e uma caneta/maquina de escrever

del escritor

# Caneta e maquina funcionam mesmo depois de apagar a classe escritor
print(caneta.brand)
maquina.write(maquina)
