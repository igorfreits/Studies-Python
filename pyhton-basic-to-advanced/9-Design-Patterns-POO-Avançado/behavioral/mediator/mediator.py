"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str

    @abstractmethod
    def broadcast(self, message: str) -> None: pass

    @abstractmethod
    def direct(self, message: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, message: str) -> None:
        self.mediator.broadcast(self, message)

    def send_direct(self, receiver: str, message: str) -> None:
        self.mediator.direct(self, receiver, message)

    def direct(self, message: str) -> None:
        print(message)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, message: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str,
               message: str) -> None: pass


class Chatroom(Mediator):  # Concrete Mediator
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, message: str) -> None:
        if not self.is_colleague(colleague):
            return
        print(f'{colleague.name} said: {message}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} for {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    chat = Chatroom()

    john = Person('John', chat)
    igor = Person('Igor', chat)
    michele = Person('Michele', chat)
    alice = Person('Alice', chat)

    chat.add(john)
    chat.add(igor)
    chat.add(michele)

    john.broadcast('Hello everyone!')
    igor.broadcast('Hello my friend!')
    alice.broadcast('I was not added to the chat...')

    print()

    igor.send_direct('Michele', 'Hello Michele!')
    michele.send_direct('Igor', 'Hello Igor!')
