"""
Invertendo valores nas variaveis
"""

x = 10
y = 'Igor'
a = 'Freitas'

z = x
x = y
y = z

print(f'x={x} e y={y}')

x, y = y, x  #
print(f'{x} e {y}')  # forma simplificada

x, y, a = a, x,  y

print(f'{x} {y} {a}')
