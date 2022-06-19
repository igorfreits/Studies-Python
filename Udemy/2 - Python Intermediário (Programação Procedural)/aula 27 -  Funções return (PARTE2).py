"""
Funções (def) - return (Parte 2)
"""
def funcao(var):
    return var
    # Tudo abaixo do return na função nao sera executado
    print('Não sera executado')


variavel = funcao('Valor que eu quero')

# Quando chega no final da função e não encontra o "return" ela retorna "None"
print(variavel)

# None = Não tem um valor

if variavel:  # if consta "None" como valor False
    print(variavel)
else:
    print('Nenhum valor')


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(8, 4)
print(divide)

if divide:
    print('Conta Valida')
else:
    print('Conta invalida')


def dumb1():
    return 1  # Função dumb1() - Consta como "int"


print(dumb1(), type(dumb1()))


def dumb2():
    return [1, 2, 3]


print(dumb2(), type(dumb2()))  # Função dumb2() - Consta como "list"


def dumb3():
    return  # Return vazio


print(dumb3(), type(dumb3()))  # Função dumb3() - Consta como "NoneType"


def a(var):
    print(var)


def b():
    return a  # Como não conterm os () não sera executado


print(type(a))

var = b()
print(var)
print(type(var))
print(id(var), id(a))
var('Pode imprimir algo')

if var == a:
    print('var é igual a A')
else:
    ('Blaaaaaaaa')


def g():
    return 'Igor', 'Michele'


print(g())

var1 = g()
print(var1, type(var1))  # Retorna uma tupla (Tupla não pode ser alterada)
