from abc import ABC, abstractmethod
""" Polimorfismo de sobreposição(POO)"""

"""Polimorfismo é p principio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos
diferente
Mesma assinatura = mesma quantidade e tipo de parâmetros"""
# Baseado na aula 66 - Classes Abstratas(POO)

"""
-Cont - Superclasse(Abstrata)
Contem o método balance(sacar) que tem a assinatura(sacar e valor)

-Todas as classes que herdarem precisam criar o corpo
do método to_withdraw(Sacar)

-SavingsAccount tem a mesma assinatura do método e to_withdraw,
mas modificou o corpo

-SavingsAccount(Conta poupança)
escreveu o corpo ja que to_withdraw nao tem corpo

-CheckingAccount(Conta corrente)
tem a mesma assinatura do método e to_withdraw e SavingsAccount,
mas tem um limite"""

# O python so suporta o polimorfismo de sobreposição
# Classe B e C tem a mesma assinatura da classe A, mas com corpo modificado


class A(ABC):  # superclasse
    @abstractmethod
    def speak(self, msg): pass


class B(A):
    def speak(self, msg):  # Polimorfismo
        print(f'B esta falando {msg}')


class C(A):
    def speak(self, msg):  # Polimorfismo
        print(f'C esta falando {msg}')


b = B()
c = C()

b.speak('UM ASSUNTO')
c.speak('OUTRO ASSUNTO')
