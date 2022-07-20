"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IOberservable(ABC):  # Observable
    @abstractmethod
    def add_observer(self, oberserver: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, oberserver: IObserver) -> None: pass

    @abstractmethod
    def notify_observer(self) -> None: pass


class WheatherStation(IOberservable):  # ConcreteObservable
    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_Update: Dict) -> None:
        # Desempacotamento de argumentos
        new_state: Dict = {**self._state, **state_Update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observer()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observer()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()
        print()


class IObserver(ABC):  # Observer
    @abstractmethod
    def update(self): pass


class Smartphone(IObserver):  # ConcreteObserver
    def __init__(self, name, observable: IObserver) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f"{self.name} recebeu uma atualização do {observable_name}"
              f" com o estado: {self.observable.state}")


if __name__ == "__main__":
    wheather_station = WheatherStation()

    smartphone_1 = Smartphone("Smartphone 1", wheather_station)
    smartphone_2 = Smartphone("Smartphone 2", wheather_station)

    wheather_station.add_observer(smartphone_1)
    wheather_station.add_observer(smartphone_2)

    wheather_station.state = {"temperature": '20'}
    wheather_station.state = {"temperature": '30', "humidity": '50'}

    wheather_station.remove_observer(smartphone_1)
    wheather_station.state = {"temperature": '40', "humidity": '70'}

    wheather_station.reset_state()
