"""Metacaracteres"""

import re
# METACARACTERES: . ^ $ * + ? { } [ ] \ | ( )

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
print(re.findall(r'João|Maria|adultos', texto))  # | = OR

# . = qualquer caractere(Com exceção da quebra de linhas)
print(re.findall(r'ad....s', texto))

print(re.findall(r'[Jj]oão', texto))  # [] = Conjunto de caracteres

print(re.findall(r'[a-zA-Z]aria', texto))  # Qual caractere entre a-z
print(re.findall(r'[0-9]aria', texto))  # Qual caractere entre 0-9

# flags=re.I, ignorar maiúsculas e minúsculas
print(re.findall(r'jOãO|MaRIa', texto, flags=re.I))
