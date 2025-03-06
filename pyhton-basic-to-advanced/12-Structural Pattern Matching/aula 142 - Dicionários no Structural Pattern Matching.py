"""Dicionários no Structural Pattern Matching"""


def execute_command(command):
    match command:
        case{'command': 'ls', 'directories': [_, *_]}:
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _:
            print('$ command  not implemented')

    print('...rest of the code')
    print()


execute_command({'command': 'ls', 'directories': ['/home', '/Users', '/etc']})
