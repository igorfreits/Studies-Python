"""
Dictionary Comprehension
"""
lista = [
    ('chave1', 'valor1'),
    ('chave2',  'valor2'),
]

""" x = chave
    y = valor

Então aqui eu estou fazendo uma compreensão de dicionário,
estou criando uma chave e um valor para
chave e valor que estão na minha lista"""

d1 = {x: y for x, y in lista}
print(d1)

d2 = {x: y*2 for x, y in lista}  # Duplica o valor Y
print(d2)

d3 = {x.upper(): y.upper() for x, y in lista}  # maiúsculo
print(d3)

lista2 = [
    ('chave1', 2),
    ('chave2', 'valor2'),
]

d4 = {x: y*2 for x, y in lista2}  # multiplica
print(d4)

d5 = {x: y for x, y in enumerate(range(5))}
print(d5)

d6 = {f'chave_{x}': x**2 for x in range(5)}
print(d6)
