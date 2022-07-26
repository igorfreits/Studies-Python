"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):  # Subject interface
    firstname: str
    lastname: str

    @abstractmethod
    def get_address(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):  # Real Subject
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # simulando requisição ao servidor
        self.firstname = firstname
        self.lastname = lastname

    def get_address(self) -> List[Dict]:
        sleep(2)  # simulando requisição ao servidor
        return [
            {'street': 'Rua dos Bobos', 'number': '123'}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # simulando requisição ao servidor
        return{
            'cpf': '123.456.789-00',
            'rg': '123456789',
        }


class UserProxy(IUser):  # Proxy
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        # Esse objetos ainda não existem nesse ponto do código
        self._real_user: RealUser  # instanciação preguiçosa
        self._cache_address: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_address(self) -> List[Dict]:
        self.get_real_user()
        if not hasattr(self, '_cache_address'):
            self._cache_address = self._real_user.get_address()
        return self._cache_address

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data


if __name__ == '__main__':
    igor = UserProxy('Igor', 'Freitas')
    print(igor.firstname)
    print(igor.lastname)

    # 6 seconds
    print(igor.get_all_user_data())
    print(igor.get_address())

    # Responde imediatamente
    print('CACHED DATA')
    for i in range(10):
        print(igor.get_all_user_data())
        print(igor.get_address())
