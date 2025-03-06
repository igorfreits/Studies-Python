"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo esta buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular esta buscando o cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular esta buscando o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo esta buscando o cliente...')


class VeiculoFactory(ABC):  # Creator
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo: pass  # Factory Method

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):  # Concrete Creator
    # Abstrai o VeiculoFactory para criação de filiais
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'Luxo':
            return CarroLuxo()
        if tipo == 'Popular':
            return CarroPopular()
        if tipo == 'Moto_popular':
            return MotoPopular()
        if tipo == 'Moto_luxo':
            return MotoLuxo()
        assert 0, 'Veiculo não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):  # Concrete Creator
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'


if __name__ == '__main__':
    from random import choice
    veiculos_zona_norte = ['Luxo', 'Popular', 'Moto_popular', 'Moto_luxo']
    veiculos_zona_sul = ['popular']

    print('Zona Norte')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_zona_norte))
        carro.buscar_cliente()

    print()

    print('Zona Sul')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_zona_sul))
        carro2.buscar_cliente()
