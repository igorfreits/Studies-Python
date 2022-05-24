"""
Expressão condicional com operador OR
"""

# Strings vazias tem o valor de False

nome = input('Digite o seu nome: ')

if nome:
    print(nome)
else:

    print('Voce não digitou nada!')

print(nome or 'Voce não digitou nada!')  # Resumo do códigoacima

print(nome or None or False or 0 or 'Voce não digitou nada' or 'Outra coisa')

a = 0
b = None
c = False
d = []
e = {}
f = 23
g = 'Colomk'

variavel = a or b or c or d or e or f or g

print(variavel)  # ira parar no primeiro valor verdadeiro
