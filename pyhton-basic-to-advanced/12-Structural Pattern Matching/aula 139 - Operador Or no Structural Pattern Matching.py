"""Operador Or no Structural Pattern Matching"""


def execute_command(command):
    match command.split():
        case['ls' | 'list', *directories]:
            for directory in directories:
                print('$ listing files from', directory)
        case['cd' | 'change', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command  not implemented')

    print('...rest of the code')


execute_command('ls /home /Users /etc')
execute_command('change /home')
