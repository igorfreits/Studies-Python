"""Random - números aleatórios e mais"""

import random
import string
"""Este módulo implementa geradores de números
pseudoaleatórios para várias distribuições.

-https://docs.python.org/pt-br/3.7/library/random.html"""

"""
O módulo string contém uma classe Template que oferece ainda outra maneira
de substituir valores em strings, usando espaços reservados como $x e
substituindo-os por valores de um dicionário, mas oferece muito menos controle da formatação.

-https://docs.python.org/pt-br/3/library/string.html"""

# Gera um numero int entre A e B
whole1 = random.randint(10, 20)
# Gera um numero aleatório usando a função range() - Inicio, final, skip
whole2 = random.randrange(900, 1000, 10)
# Gera um numero float entre A e B
floating1 = random.uniform(10, 20)
# Gera um numero float entre 0 e 1
floating2 = random.random()

print(whole1)  # Inteiro
print(whole2)
print(floating1)
print(floating2)

list = ['Igor', 'Michele', 'Noah', 'Isra', 'Alice']
prize_draw1 = random.choice(list)  # Sorteio
# Retorna dois itens aleatórios
prize_draw2 = random.choices(list, k=2)  # Retorna dois itens aleatórios
# Retorna dois itens aleatórios que nao se repete
prize_draw3 = random.sample(list, 2)
print(prize_draw1)
print(prize_draw2)
print(prize_draw3)

print()

# for i in range(1000):
#     prize_draw4 = random.sample(list, 2)
#     print(prize_draw4)

random.shuffle(list)  # Embaralha a lista
print(list)

# Gera senha aleatória
letter = string.ascii_letters  # Letra
digits = string.digits  # Dígitos
characters = '!@#$%^&*._-'  # Caracteres

general = letter + digits + characters
password = "".join(random.choices(general, k=20))
print(password)
