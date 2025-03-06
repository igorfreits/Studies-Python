"""Usando listas e mais alguns exemplos de Structural Pattern Matching"""


def execute_command(command):
    match command.split():
        case['ls', *directories, '--force', _]:
            for directory in directories:
                print('$ listing files FORCED', directory)
        case['ls', *directories]:
            for directory in directories:
                print('$ listing files', directory)
        case['cd', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command  not implemented')


execute_command('ls /home /Users /etc --force --create')
execute_command('ls /home /Users /etc')
