"""
For - Estrutura de repetição finita
"""
# laço com variável de controle
# laço c no intervalo(1,6): - a variável pode conter qualquer valor - Portugol
# range (inicio, fim , passo)
# Aninhar - coloca um estrutura dentro da outra (if, elif, else)

"""
laço c no intervalo de (0,3):  # aninhar
se "moeda"
    pega
passo
"""

for c in range(1, 6):  # Nao considera o ultimo numero
    print('Oie')

print('###')

for c in range(6, 0, -1):  # Conta de trás para frente
    print(c)

print('###')

for c in range(0, 7, 2):  # Pula de dois em dois
    print(c)

print('###')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)

print('###')

i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f, p):
    print(c)

print('###')

for c in range(0, 3):
    n = int(input('Digite um valor: '))

print('###')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n  # (s = s+n)
    print(f'A soma de todos os valores foi de {s}')
