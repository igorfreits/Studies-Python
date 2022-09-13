"""Comparando Pattern Matching com IF, ELIF e ELSE ou SWITCH CASE"""


def execute_command1(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')

    print('...rest of the code')


# execute_command1('ls')

def execute_command2(command: str):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case  _:  # Não Obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command2('pwd')
