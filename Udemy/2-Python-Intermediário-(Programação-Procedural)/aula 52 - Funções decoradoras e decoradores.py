"""
Funções decoradoras e decoradores
"""
from time import time


# Funções como variáveis
def fala_oi():
    print('Oi')


# A variável é igual a função
variável = fala_oi
print(type(variável))  # function
variável()  # Oi


# Uma função dentro de outra


def master():
    # Função interna
    def slave():
        print('Oi')
    # Função a ser executada
    return slave


# Variável recebe função
variável = master()
# Executa a função interna de master
variável()

# Função como parâmetro


def master(função):
    # Função interna
    def slave():
        # executa a função enviada
        função()
    # Retorna a função interna sem executar
    return slave

# Uma função qualquer


def fala_oi():
    print('Oi')


# Variável como função
variável = master(fala_oi)
# Executa a variável/função
variável()

# Recebe uma função


def master(função):
    # Cria uma função interna
    def slave():
        # Decora
        print('Estou decorada.')
        # Executa a função enviada
        função()
    # Retorna a função interna sem executar
    return slave

# Uma função qualquer


def fala_oi():
    print('Oi')


# Decorando
fala_oi = master(fala_oi)
fala_oi()
'''

'''
# Função decoradora


def master(função):
    def slave():
        print('Estou decorada.')
        função()
    return slave

# Sintaxe sugar do decorador


@master
def fala_oi():
    print('Oi')


fala_oi()

# Decorando com parâmetros


def master(função):
    def slave(*args, **kwargs):
        print('Estou decorada.')
        função(*args, **kwargs)
    return slave


@master
def fala_oi(msg):
    print(msg)


fala_oi('Olá, sou Luiz')


def velocidade(função):
    """
    Função decoradora: Verifica o tempo que uma função leva para executar
    """
    def envolve(*args, **kwargs):
        """ Função que envolve e executa outra função """
        # Tempo inicial
        start = time()
        # Executa a função
        resultado = função(*args, **kwargs)
        # Tempo final
        end = time()
        # Resultado de tempo em ms
        tempo = (end - start) * 1000
        # Mostra o tempo
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return envolve


@velocidade
def demora(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
demora(10000)
