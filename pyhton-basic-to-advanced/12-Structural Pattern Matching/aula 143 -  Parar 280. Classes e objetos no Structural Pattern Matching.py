"""Classes e objetos no Structural Pattern Matching"""

from dataclasses import dataclass


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing directory to', directory)
        case Command(command=_, directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)

        case _:
            print('$ command  not implemented')

    print('...rest of the code')
    print()


command_1 = Command('ls', ['/home'])
command_2 = Command('cd', ['/Users'])
execute_command(command_1)
execute_command(command_2)


# print()
# execute_command(Command(command='ls', directories=['/home', '/Users', '/etc']))
# execute_command(Command(command='cd', directories=['/home', '/Users', '/etc']))
