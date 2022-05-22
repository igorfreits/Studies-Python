from math import factorial  # Com o uso da biblioteca
n = int(input('Digite um numero para ser fatorado: '))
fatorial = factorial(n)
print(fatorial)

# com o uso do laco while
f = 1
c = n
print(f'Calculando {c}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
