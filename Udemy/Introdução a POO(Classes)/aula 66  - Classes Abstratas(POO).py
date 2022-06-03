"""Classes Abstratas(POO)"""
from abc import ABC, abstractmethod
"""Classe Abstrata
-Pode ter métodos concretos e métodos abstratos

-O método abstrato é um contrato, você está basicamente informando que esse
método não foi implementado ainda e que precisa ser implementado
nas subclasses
Ele é bastante usado em abstrações em geral e padrões de projeto.

-Um método abstrato é um método que não tem corpo geralmente que você
criou o método não escreve o código
dele você simplesmente fala que ele é abstrato para que as outras
classes filhas deem esse método e
sejam obrigadas a criar esse método dentro das classes filhas mesmo

-Métodos concretos são métodos normais que você escreve
código e ele funciona perfeitamente na cadeia de heranças

"""


class A(ABC):
    @abstractmethod
# força para que todas as classes que herdarem de A deve ter o método "speak"
    def speak(self):
        pass


"""Quando eu tenho um método abstrato numa classe eu
não posso mais instanciar ela"""


class B(A):
    def speak(self):
        print('Falando...')


a = B()
a.speak()

print('-+'*30)


class Cont(ABC):
    # Agencia, conta, saldo
    def __init__(self, agency, cont, balance):
        self._agency = agency
        self._cont = cont
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def cont(self):
        return self._cont

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        # Verifica se value e uma instancia de int ou float
        if not isinstance(value, (int, float)):

            # Saldo precisa ser numérico
            raise ValueError('balance must be numeric')
        self._balance = value

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            # valor do depósito precisa ser numérico
            raise ValueError('deposit amount must be numeric')
        self._balance += value
        self.details()

    def details(self):
        print(f'Agency: {self.agency}', end=' ')  # Agencia
        print(f'Cont: {self.cont}', end=' ')  # Conta
        print(f'balance: {self.balance}')  # Saldo

    @abstractmethod
    def to_withdraw(self, value):  # Sacar
        pass


class SavingsAccount(Cont):  # Conta poupança
    def to_withdraw(self, value):  # Sacar
        if self.balance < value:
            print('insufficient funds')  # Saldo insuficiente
            return
        self.balance -= value
        self.details()


cp = SavingsAccount(1111, 2222, 0)  # Agency, cont, balance
cp.deposit(10)
cp.to_withdraw(5)
cp.to_withdraw(5)
cp.to_withdraw(5)

print('-+'*30)


class CheckingAccount(Cont):  # Conta corrente
    def __init__(self, agency, cont, balance, limit=100):
        super().__init__(agency, cont, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def to_withdraw(self, value):  # Sacar
        if (self.balance + self.limit) < value:
            print('insufficient funds')  # Saldo insuficiente
            return
        self.balance -= value
        self.details()


cc = CheckingAccount(agency=1111, cont=3333, balance=0, limit=500)
cc.deposit(100)
cc.to_withdraw(250)
cc.to_withdraw(500)
cc.deposit(1000)
