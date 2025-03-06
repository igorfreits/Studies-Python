"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""
from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN esta buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN esta buscando o cliente...')


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZN esta buscando o cliente...')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN esta buscando o cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS esta buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS esta buscando o cliente...')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS esta buscando o cliente...')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS esta buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod
    def get_carro_moto_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_carro_moto_popular() -> VeiculoPopular: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    # Famílias de objetos
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:  # Factory Method
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:  # Factory Method
        return CarroPopularZN()

    @staticmethod
    def get_carro_moto_luxo() -> VeiculoLuxo:  # Factory Method
        return MotoLuxoZN()

    @staticmethod
    def get_carro_moto_popular() -> VeiculoPopular:  # Factory Method
        return MotoPopularZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    # Famílias de objetos
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:  # Factory Method
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:  # Factory Method
        return CarroPopularZS()

    @staticmethod
    def get_carro_moto_luxo() -> VeiculoLuxo:  # Factory Method
        return MotoLuxoZS()

    @staticmethod
    def get_carro_moto_popular() -> VeiculoPopular:  # Factory Method
        return MotoPopularZS()


class Cliente:  # composição
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_carro_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_carro_moto_luxo()
            moto_luxo.buscar_cliente()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.busca_clientes()
