"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou Conta Poupança)
Criar classes Conta Poupança e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from abc import abstractmethod, ABC


class People:
    def __init__(self, name, age):
        self._name = name  # Encapsulamento
        self._age = age

    @property  # getter
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Client(People):  # Herança
    def __init__(self, name, age):
        super().__init__(name, age)
        self.cont = None

    def insert_account(self,  cont):
        self.cont = cont


class Cont(ABC):  # Abstração
    def __init__(self, agency, cont, balance):
        self.agency = agency
        self.cont = cont
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        self.details()

    def details(self):
        print(f'Agency: {self.agency} '
              f'Cont: {self.cont} '
              f'Balance: {self.balance}')

    @abstractmethod  # Abstração
    def to_withdraw(self, value): pass


class SavingsAccount(Cont):
    def to_withdraw(self, value):  # Polimorfismo
        if self.balance < value:
            print('insufficient funds')
            return
        self.balance -= value
        self.details()


class CheckingAccount(Cont):
    def __init__(self, agency, cont, balance, limit=100):
        super().__init__(agency, cont, balance)
        self.limit = limit

    def to_withdraw(self, value):  # Polimorfismo
        if (self.balance + self.limit) < value:
            print('insufficient funds')
            return
        self.balance -= value
        self.details()


class Bank:  # agregação
    def __init__(self):
        self.agencies = (1111, 2222, 3333)
        self.clients = []
        self.bills = []  # Contas

    def insert_account(self, client):
        self.bills.append(client)

    def insert_clients(self, cont):
        self.clients.append(cont)

    def authenticate(self, client):
        if client not in self.clients:
            return False

        if client.cont not in self.bills:
            return False

        if client.cont.agency not in self.agencies:
            return False
        return True


# ----------------------------------------------------------------
bank = Bank()

client1 = Client('Luiz', 30)
client2 = Client('Maria', 18)
cliente3 = Client('João', 50)

cont1 = SavingsAccount(1111, 254136, 0)
cont2 = CheckingAccount(2222, 254137, 0)
cont3 = SavingsAccount(1212, 254138, 0)

client1.insert_account(cont1)
client2.insert_account(cont2)
cliente3.insert_account(cont3)

bank.insert_clients(client1)
bank.insert_account(cont1)

bank.insert_clients(client2)
bank.insert_account(cont2)

if bank.authenticate(client1):
    client1.cont.deposit(0)
    client1.cont.to_withdraw(20)
else:
    print('unauthenticated client')  # cliente não autenticado

print('####################')

if bank.authenticate(client2):
    client2.cont.deposit(0)
    client2.cont.to_withdraw(30)
else:
    print('unauthenticated client')  # cliente não autenticado
