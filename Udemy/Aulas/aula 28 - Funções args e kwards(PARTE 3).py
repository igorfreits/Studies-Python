"""
Funções (def) *args **kwargs (Parte 3)
"""

# Revisão
# def func(a1=1, a2=2, a3):  # No momento que se seta um padrão pra função os proximo também devem ter um padrão
#     print(a1, a2, a3)


# func(1, a2=5, a3) # Depois de nomear um argumentos  todos depois deles devem ser nomeado

def func1(a1=None, a2=123):  # Valor None numa variavel retorna None
    print(a1, a2)
    return a1


# Para a variavel retorne algum valor devesse colocar o return e o parametro que retorna None

var = func1(46, a2='Caneca')
print(var)

"""Use args e kwargs quando uma função precisar receber um número indefinido de parâmetros.

A diferença entre args e kwargs é simplesmente se o parâmetro é ou não nomeado.
Se não for um parâmetro nomeado, cai em args, se for nomeado cai em kwargs."""


def func2(*args):  # Pode usar outro nome além de args, mas deve ter o *
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


func2(1, 2, 3, 4, 5)

# *args = A variavel com * representa uma lista
# ***kwarg = A variavel com ** representa um dicionario


# def sem_args(n1):
#     print(n1)

# sem_args(4, 'Igor', 77) # Erro - nao foi definido o 3 argumento  na função


def a1(*args):
    # Converte o valor em um lista, pois args é considerado uma tupla
    args = list(args)
    args[0] = 20
    print(args)


a1(1, 2, 3, 4, 5,)


def a2(*args):
    print(args)  # Para acessa a lista é preciso adicionar o [0]


lista1 = [1, 2, 3, 4, 5]
a2(*lista1, 10, 20, 30, 40, 50)
# Cada elemento apos o *lista entra na lista da tupla
lista2 = [10, 11, 12, 13, 14, 15]
a2(*lista1, *lista2)  # As listas serão desempacotadas


def a3(*args, **kwargs):
    print(args)
    print(kwargs)  # Para parametros nomeados


a3(1, 2, 3, nome='Igor', sobrenome='Freitas')


def a4(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')  # Verifica se tem o parametro nome
    print(nome)


a4(1, 2, 3, 4, 5, nome='Igor')


def a5(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


a5(5, 4, 3, 2, 1, nome='Igor', idade=25)
