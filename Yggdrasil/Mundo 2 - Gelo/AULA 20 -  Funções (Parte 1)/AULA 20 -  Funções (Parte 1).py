"""
def - Definição de função personalizada(Rotina)
"""


from operator import le


def mostra_linha():
    print('-' * 30)
# Sempre que for usado o "mostra_linha() sera executado o print()"


# def sempre pede 2 espaços entre as linhas
# Programa principal
mostra_linha()
print('         Game Over       ')
mostra_linha()
mostra_linha()
print('           Igor        ')
mostra_linha()

print()


def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


# Parametros
mensagem('Curso em video')
mensagem('Python é muito bom')


def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} é {s}')


# programa principal
soma(4, 6)
soma(b=4, a=5)  # Sempre deve explicitar os parametros

# soma(4) - sempre deve haver 2 parametros


def contador(*num):  # * = desempacotar = Joga o excesso de valores no *num
    tam = len(num)
    print(f' Recebi os valores {num} e são ao todo {tam} numeros')


# Foi criado uma tupla
contador(1, 2, 3)
contador(4, 5, 6, 7)
contador(100, 51, 60, 13, 10)


def dobra(lst):  # Tudo feito no lst interfere a a lista valores
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
