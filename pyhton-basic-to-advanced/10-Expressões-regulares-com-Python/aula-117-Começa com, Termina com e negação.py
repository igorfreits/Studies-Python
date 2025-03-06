"""Começa com, Termina com e negação"""

import re
# ^ - Começa com
# $ - Termina com
# [^a-z] - Negação - Deve estar no inicio do conjunto(Nada que tenha entre a e z)

cpf = '123.456.789-10'
# verifica se o cpf é valido(deve estar igual a expressão regular)
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]', cpf))  # Nada que não seja um número
