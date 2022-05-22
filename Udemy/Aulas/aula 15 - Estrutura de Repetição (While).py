"""
while
Utilizado para realizar ações enquanto uma condição for verdadeira.

Requisitos: Entender condições e operadores

while condição:
"""

"""while True:  # loop infinito
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}!')"""

x = 0
while x <= 10:  # mostra valor de 0 ate 10
    if x == 3:
        x = x + 1
        # continue  # Não executa as linhas posteriores e volta pro loop (mostra o valor 3 infinitamente)
        # break  # Finalina o loop (Para quando o valor 3 for Verdadeira)
    print(x)
    x = x + 1
print('Acabou!')

a = 0  # coluna
while a < 10:
    b = 0  # linha

    while b < 5:
        print(f'A é igual a {a} e B vale {b}')
        print(f'({a}, {b})')
        b += 1
    a += 1  # a = a +1
print('Fim!')

while True:
    print()
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    operador = input('Digitar um operador: ')
    sair = input('Deseja Sair? [S]im ou [N]ão'
                 '\n...')

    if sair == 's':
        break

    if not n1.isnumeric() or not n2.isnumeric():
        # se n1 e n2 nao for um numero nao sera executado
        print('Voce precisa digitar um numero')
        continue

    n1 = int(n1)
    n2 = int(n2)

    #  + - / *
    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '/':
        print(n1 / n2)
    elif operador == '*':
        print(n1 * n2)
