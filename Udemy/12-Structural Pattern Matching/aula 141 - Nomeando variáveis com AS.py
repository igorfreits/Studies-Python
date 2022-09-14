"""Nomeando variáveis com AS"""


def execute_command(command):
    match command.split():
        case['ls' | 'list' as the_command, *directories]as the_list if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
            print(f'{the_command},{the_list}')
        case['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case['cd', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command  not implemented')

    print('...rest of the code')
    print()


execute_command('ls /home /Users /etc')
execute_command('ls /home')
execute_command('cd /home')
