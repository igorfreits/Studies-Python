""" Herança múltipla"""

# Herda atributos de múltiplas classes
"""# Problema do diamante: uma classe que tem herança múltipla
herda de duas classes que tem o mesmo método

Em teoria a gente não saberia qual dos métodos será chamado
Em python a herança múltipla ele busca da esquerda pra direita
"""


class A:
    def speak(self):
        print('Falando...Estou em A')


class B(A):  # Herança simples de A
    def speak(self):
        print('Falando...Estou em B')  # Sobrescrevendo


class C(A):  # Herança simples de A
    def speak(self):
        print('Falando...Estou em C')  # Sobrescrevendo


class D(B, C):  # Herança múltipla de  B, C
    pass


d = D()
d.speak()  # Chama o método B(Mesmo herdando de B e C)

"""Nesse caso ele vai procurar primeiro em B se ele achar o método
que eu estou procurando que no caso é falar em B.(Sera executado)

Se ele não encontrar em B ele vai procurar em C.

Mas se caso ele nao achar o método ele ira procurar em A porque o C herda de A
"""
print('-='*50)
"""Classe mixin
-Não  é uma classe abstrata
-Não foi feita pra ser instanciada diretamente
-Classe mixin vai ter por exemplo uma funcionalidade adicional
que eu quero adicionar em outra classe
-Não esta presente na hierarquia de classes
"""

# Sistema de login


class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


class Electronic:
    def __init__(self, name):
        self._name = name
        self._switched_on = False  # Ligado

    def turn_on(self):  # Ligar
        if self._switched_on:
            return
        self._switched_on = True

    def turn_off(self):  # Desligar
        if not self._switched_on:
            return
        self._switched_on = False


class Smartphone(Electronic, LogMixin):  # Herança simples de Electronic
    def __init__(self, nome):
        super().__init__(nome)
        self._connected = False

    def connect(self):
        if not self.turn_on:
            info = f'{self._name} não está ligado'
            print(info)
            self.log_error(info)
            return

        if self._connected:  # Verifica se esta ligado
            error = f'{self._name} JÁ ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._name} ESTÁ CONECTADO.'
        print(info)
        self.log_info(info)
        self._connected = True

    def disconnect(self):
        if not self._connected:
            error = f'{self._name} NÃO ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._name} foi deligado com sucesso.'
        print(info)
        self.log_info(info)
        self._connected = False


smartphone = Smartphone('Pocophone X3 PRO')
smartphone.connect()
smartphone.turn_off()
smartphone.turn_on()
smartphone.connect()
smartphone.connect()
smartphone.connect()
smartphone.turn_off()
smartphone.connect()
smartphone.disconnect()
smartphone.disconnect()
