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
