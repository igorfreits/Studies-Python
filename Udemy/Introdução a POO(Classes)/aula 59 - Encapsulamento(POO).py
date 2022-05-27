"""Encapsulamento"""

# Encapsulamento - proteger/esconder partes do código

# Modificadores de acesso
# métodos/atributos - public, private, protected

# public - acessados dentro e fora da classe
# protected - acessadas dentro a classe ou das filhas da classe(herança)
# private - Disponível apenas dentro da classe

# convenções :  _ protected e __ private


class BaseDeDados:  # Constructor
    def __init__(self):
        self.__dados = {}  # private

    @property
    def dados(self):
        return self.__dados

    def insert_clients(self, id, name):
        # Confere se a chave não esta no dicionario
        if 'clients' not in self.__dados:
            self.__dados['clients'] = {id: name}  # keys: name
        else:
            self.__dados['clients'].update({id: name})

    def list_clients(self):
        for id, name in self.__dados['clients'].items():
            print(id, name)

    def erase_client(self, id):
        del self.__dados['clients'][id]


bd = BaseDeDados()
bd.insert_clients(1, 'Igor')
bd.insert_clients(2, 'Michele')
bd.insert_clients(3, 'Noah')
bd.__dados = 'Outra coisa'  # Cria um novo atributo e nao quebra o código
print(bd.__dados)
# bd.dados = 'Outra coisa' - Se for mudado valor o código inteiro quebra
print(bd._BaseDeDados__dados)
