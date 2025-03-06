"""Grupos e Retrovisores"""

import re
from pprint import pprint

# (abc|def) - Grupos (Encontra abc ou def)
# Grupos ficam dentro de parenteses
# Retrovisores são acessados com o carácter '\'
# Contar as aberturas dos parenteses
# ?: - Ignora o grupo(Não salva o grupo)

# () - \1
# () () - \1,\2
# (())() - \1,\2,\3

texto = ''''
<p>Frase</p> <p>phrase</p> <p>段階</p> <div>фраза</div> <div></div>
'''
# Não salva o grupo na memoria(Usando o ?:)
# cpf = 'A 123.456.789-10 A'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags1 = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>', texto)
# pprint(tags1)

# Grupo nomeado
# tags2 = re.findall(r'<(?P<tag>[pdiv]{1,3})>(?:.+?)<\/(?P=tag)>', texto)
# pprint(tags2)
print(re.sub(r'(<(.+?)>)(.?)(</\2>)', r'\1 \3 \4', texto))
# for tag in tags1:
#     um, dois, tres = tag
#     print(tres)
