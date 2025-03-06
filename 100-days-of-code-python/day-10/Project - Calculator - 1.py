# Calculator

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

num1 = int(input('Qual o primeiro número? '))
num2 = int(input('Qual o segundo número? '))

for symbol in operations:
    print(symbol)

operation_symbol = input('Qual operação você deseja realizar? ')

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer} ')
