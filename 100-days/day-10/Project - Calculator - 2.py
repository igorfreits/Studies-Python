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

first_answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {first_answer} ')

simbol_operation = input('Qual operação você deseja realizar? ')
num3 = int(input('Qual o próximo número? '))

calculation_function = operations[simbol_operation]

second_answer = calculation_function(calculation_function(num1, num2), num3)

print(f'{first_answer} {simbol_operation} {num3} = {second_answer} ')
