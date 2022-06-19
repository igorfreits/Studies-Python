"""
Escopo global e local
"""

# Escopo global(Esta acessível a todos os locais na aplicação)
variavel = 'valor'


def a1():
    print(variavel)


def a2():
    # global variavel - NÂO RECOMENDÁVEL (Afeta a varinel global)
    variavel = 'Outro Valor'  # Escopo local(Esta accessível somente na função)
    print(variavel)


a1()  # GLobal
a2()  # Local - Não é possível editar dentro de um função
print(variavel)


def a3(arg=None):
    arg = arg.replace('v', 'c')
    return arg


outra_variavel = a3(arg=variavel)
print(outra_variavel)  # Pega o valor da variavel, mas nao altera


# def a4():
#     print(variavel)
#     variavel = 123 - Valor ja havia sido definido
#     print(variavel)


# a4()
"""UnboundLocalError: local variable 'variavel' referenced before assignment"""


def a():
    a = 'valor'


def b():
    print(a)  # não é possível acessar variaveis que estão dentro de outras funções


def c():
    c = 'E = mc²'
    return c


def d(arg):
    print(arg)


var1 = c()
d(var1)
# Conecta duas funções
