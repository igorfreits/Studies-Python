"""
Expressão condicional com operador OR
"""

# Strings vazias tem o valor de False

nome = input('Digite o seu nome: ')

if nome:
    print(nome)
else:

    print('Voce não digitou nada!')

print(nome or 'Voce não digitou nada!')  # Resumo do código acima

print(nome or None or False or 0 or 'Voce não digitou nada' or 'Outra coisa')

a = 0
b = None
c = False
d = []
e = {}
f = 23
g = 'Colomk'

variável = a or b or c or d or e or f or g

print(variável)  # ira parar no primeiro valor verdadeiro
