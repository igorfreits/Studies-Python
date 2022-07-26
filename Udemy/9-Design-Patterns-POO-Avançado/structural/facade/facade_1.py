"""
Façade (Fachada) é um padrão de projeto estrutural
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser
usado.
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


class WatherStationFacade:  # Facade
    def __init__(self) -> None:
        self.wheather_station = WheatherStation()

        self.smartphone_1 = Smartphone("Smartphone 1", self.wheather_station)
        self.smartphone_2 = Smartphone("Smartphone 2", self.wheather_station)

        self.wheather_station.add_observer(self.smartphone_1)
        self.wheather_station.add_observer(self.smartphone_2)

    def add_observer(self, observer: IObserver) -> None:
        self.wheather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.wheather_station.remove_observer(observer)

    def change_state(self, state: Dict) -> None:
        self.wheather_station.state = state

    def remove_smartphone(self) -> None:
        self.wheather_station.remove_observer(self.smartphone_1)

    def reset_state(self) -> None:
        self.wheather_station.reset_state()


if __name__ == "__main__":
    wheather_station = WatherStationFacade()

    wheather_station.change_state({"temperature": '20'})
    wheather_station.change_state({"temperature": '30'})
    wheather_station.change_state({"temperature": '40'})

    wheather_station.remove_smartphone()

    wheather_station.change_state({"temperature": '20'})
    wheather_station.change_state({"temperature": '30'})
    wheather_station.change_state({"temperature": '40'})

    wheather_station.reset_state()
    wheather_station.change_state({"temperature": '20'})
    wheather_station.change_state({"temperature": '30'})
    wheather_station.change_state({"temperature": '40'})
