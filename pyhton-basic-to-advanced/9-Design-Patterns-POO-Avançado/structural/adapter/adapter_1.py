"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""
from abc import ABC, abstractmethod
from hashlib import new


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print("moving to...top")

    def down(self) -> None:
        print("moving to...down")

    def left(self) -> None:
        print("moving to...left")

    def right(self) -> None:
        print("moving to...right")


class NewControl:
    def move_top(self) -> None:
        print("\033[34m New Control:\033[m moving to...top")

    def move_down(self) -> None:
        print("\033[34m New Control:\033[m moving to...down")

    def move_left(self) -> None:
        print("\033[34m New Control:\033[m moving to...left")

    def move_right(self) -> None:
        print("\033[34m New Control:\033[m moving to...right")


class ControlAdapter:  # Composição
    # Adapter Object
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()

    def right(self) -> None:
        self.new_control.move_right()


class ControlAdapter2(Control, NewControl):  # Herança Múltipla
    # Adapter class
    def top(self) -> None:
        self.move_top()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()

    def right(self) -> None:
        self.move_right()


if __name__ == '__main__':
    # Control - Adapter Object
    new_control = NewControl()
    control_object = ControlAdapter(new_control)

    control_object.down()
    control_object.top()
    control_object.left()
    control_object.right()

    print()

    # Control - Adapter class
    control_class = ControlAdapter2()

    control_class.down()
    control_class.top()
    control_class.left()
    control_class.right()
