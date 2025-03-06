"""Expressões regulares com Python - Regex

-https://docs.python.org/3/library/re.html
=https://docs.python.org/3/howto/regex.html#regex-howto

"""

import re
string = 'Este é um teste com expressões regulares'
# Expressões regulares são padrões que podem ser usados para encontrar padrões em textos


# Deve passar a expressão regular como esta escrita
# Usar o r'' para evitar problemas de escape

print(re.search(r'teste', string))
# Exibi posição inicial e a final


print(re.findall(r'teste', string))
# Exibi todas as ocorrências em lista

print(re.sub(r'teste', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', string))
# Substitui todas as ocorrências

print()

regexp = re.compile(r'regulares')
# Compila a expressão regular
# OBS: O compilador não compila a expressão regular

print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('01234567890', string))
