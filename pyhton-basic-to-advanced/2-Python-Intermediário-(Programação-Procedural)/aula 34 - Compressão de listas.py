"""
List Comprehension
"""

# Compressão de listas
# otimização de performance no código escrevendo menos linhas
# Tudo em um alinha código
# Mais rápido e "simples"
# list_comprehension EXEMPLO = ["item"(variável) (condição/operação)
# PARA CADA "item" SE a condição for verdadeira]
#  for in         if

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]
print(ex1)

ex2 = [v * 2 for v in l1]
print(ex2)

# 1° for itera na lista
# 2° for itera cada elemento da lista
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ['Igor', 'Michele', 'Noah']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x)for x, y in tupla]
ex5 = dict(ex5)
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)

lista_preços = [500, 1500, 2000, 100, 25]
nova_lista_de_preços = []

# Dobrar valor
for preço in lista_preços:
    nova_lista_de_preços.append(preço * 2)
print(nova_lista_de_preços)

# Para cada "item" na minha lista adicione "item" * 2
nova_lista_de_preços = [
    preço * 2 for preço in lista_preços]  # List comprehension
print(nova_lista_de_preços)

print()

# produtos acima de 1000 dolares + 50% do valor total
imposto2 = []
for preço in lista_preços:
    if preço > 1000:
        imposto2.append(preço * 0.5)
print(imposto2)

print()

# Para cada "item" acima se 1000...adicione + 50%
imposto2 = [preço * 0.5 for preço in lista_preços if preço > 1000]
print(imposto2)
