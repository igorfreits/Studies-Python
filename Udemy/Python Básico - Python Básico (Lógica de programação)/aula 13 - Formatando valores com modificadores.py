"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. - (numero)f - quantidade de casa decimais (float)  EX: :.2f
;(caractere)(> ou < ou ^)(quantidade)(tipo - s,d ou f)

> - esquerda
< - direita
^ - centro
"""

n1 = 10
n2 = 3
divisão = n1 / n2
print('{:.2f}'.format(divisão))  # na formatação tem duas casas decimais

nome = 'Igor Freitas'
print(f'{nome:s}')

num1 = 1
print(f'{num1:0>10}')  # 000000001

num2 = 2
print(f'{num2:0<10}')  # 200000000

num3 = 3
print(f'{num3:0^10}')  # 0000300000

numero = 1150
print(f'{numero:.2f}')  # 0000300000

num4 = 4
print(f'{num4:0>10.2f}')  # 0000004.00

name = 'Igor Freitas'
print((50-len(name))/2)
print(f'{name:#^50}')

nome_formatado = '{:@>10}'.format(nome)
print(nome_formatado)
