"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""
# Meu Resultado
tarefas = []
tarefas_desfeitas = []


def adiciona():
    nova_tarefa = input('Digite o nome da tarefa: ')
    tarefas.append(nova_tarefa)
    print(f'Você adicionou a tarefa "{nova_tarefa}" a sua lista ')


def remover():
    if tarefas == []:
        print('Nada a refazer')
    else:
        print(f'Você removeu "{tarefas[-1]}" da sua lista de tarefas')
        tarefas_desfeitas.append(tarefas[-1])
        tarefas.pop()


def refazer():
    print(
        f'Você adicionou "{tarefas_desfeitas[-1]}" a sua de tarefas novamente')
    tarefas.append(tarefas_desfeitas[-1])
    tarefas_desfeitas.pop()


def lista():
    print(f'A sua lista atual contem os seguintes itens:\n{tarefas}')


while True:
    opções = int(input('Oque você desejar fazer?'
                       '\n [ 1 ] Adicionar tarefa'
                       '\n [ 2 ] Remover tarefa'
                       '\n [ 3 ] Refazer tarefa'
                       '\n [ 4 ] Mostrar tarefas'
                       '\n [ 5 ] Terminar código'
                       '\n ...'))
    if opções == 1:
        adiciona()

    elif opções == 2:
        remover()

    elif opções == 3:
        refazer()

    elif opções == 4:
        lista()

    elif opções == 5:
        break
print(f'{"Fim do Programa":-^40}')

# Resultado do Professor


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)
