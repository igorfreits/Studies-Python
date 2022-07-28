"""Quantificadores"""

import re
# * 0 ou ilimitado
# + 1 ou ilimitado
# ? 0 ou 1
# {n} especifico
# {min, max} especifico

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
Jã
'''
# Sempre o da esquerda!
print(re.findall(r'Jo+Ão+', texto, flags=re.I))
# 1 ou mais caracteres

print(re.sub(r'Jo*Ão*', 'Felipe', texto, flags=re.I))
# 0 ou ilimitadas vezes

print(re.sub(r'Jo?Ão?', 'Lucas', texto, flags=re.I))
# 0 ou 1 vez

print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# {mínimo, máximo}

texto2 = 'Igor ama ser amado'
print(re.findall(r'ama[do]*', texto2, flags=re.I))
# Conjunto com 0 ou mais caracteres
