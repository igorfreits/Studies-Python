"""
For / Else em python
"""

variavel = ['Igor', 'joãozinho', 'Maria']

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('J'):  # .startswith = checa se existe um valor numa string
        print('Começa com "J" = ', valor)
    else:
        print('Não começa com "J" = ', valor)

for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palarva que começa com "J"')
else:
    print('Não existe uma palavra com "J"')


for valor in variavel:  # Simplificada
    print(valor)
    if valor.lower().startswith('j'):
        break  # ou continue,  mas sem o continue
    print(valor)
else:
    print('Não existe uma palavra com J')
