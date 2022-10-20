def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = int(input('Qual o primeiro número? '))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input('Qual operação você deseja realizar? ')
        num2 = int(input('Qual o segundo número? '))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer} ')

        if input(
                f'Digite "y" para continuar calculando com {answer}, ou digite "n" para iniciar um novo calculo : ') == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
