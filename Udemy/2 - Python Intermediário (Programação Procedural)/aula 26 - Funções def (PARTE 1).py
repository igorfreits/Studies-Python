"""
Funções - def (Parte 1)
"""


# def função():

def função():  # Defini a função (pode ter qualquer nome)
    print('Hello World!')  # Mostra oque a função ira fazer


# Exibi o valor da função() que foi definida
# Se trocar o valor da função() haverá alteração
função()
função()
função()
função()


def função1(parametros):  # Parametros sao variaveis
    print(parametros)


função1('oie')
função1(4)
# função1()  # nao sera executado pois nao tem a variável dentro


def saudação(msg='Ola', nome='usuário'):  # msg e nome padrão
    nome = nome.replace('e', '3')  # .replace - substitui dois valores
    msg = msg.replace('e', '3')

    print(msg, nome)


saudação('Olá', 'Igor')
saudação('Oie', 'Michele')
# Pode ser invertido, mas tem, que usar o parametro
saudação(nome='Israel', msg='Hello')
# saudação()  # Sera exibido o valor padrão

