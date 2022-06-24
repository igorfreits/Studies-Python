"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""


def hello():
    return 'Olá, mundo!'


def mestre(funcao):
    return funcao()


executando = mestre(hello)
print(executando)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def master(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = master(fala_oi, 'Igor')
executando2 = master(saudacao, 'Igor', saudacao='Bom dia!')
print(executando)
print(executando2)
