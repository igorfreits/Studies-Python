"""
Split, Join, Enumerate em Python
-Split = Dividir uma string  # str
-Join = Juntar uma lista # str
-Enumerate = Enumerar elementos da lista # list
"""

string = 'O Brasil é o pais do futebol , o Brasil é Penta!'
# split -Transforma a variavel string em lista separada com com caractere escolhido
lista1 = string.split(' ')
lista2 = string.split(',')

palavra = ' '
contagem = 0

for valor in lista1:
    # count - Quantas palavras tem
    print(f'A palavra {valor} apareceu {lista1.count(valor)}')
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que mais aparece é {palavra} ({contagem}X)')

for valor in lista2:
    print(valor.strip())  # strip - apaga excesso de espaços na direita e esquerda

string_0 = 'O Brasil é hexa'
lista3 = string_0.split(' ')
# Join - Junta os elementos da lista com caractere escolhido
string_1 = ' '.join(lista3)
print(string_0)
print(lista3)
print(string_1)

for indice, v2 in enumerate(lista3):  # enumera os elementos da lista
    print(indice, v2)

lista_a = [1, 2, 3, 4, 5, 6]
for x in lista_a:
    print(x)

lista_00 = ['Igor', 'Michele', 'Leona']
n1, n2, n3 = lista_00
print(n2)

lista_a = [
    # 0      #1      #2
    ['Igor', 'João', 'Gaby'],  # 0
    ['Maria', 'Aline', 'Michele'],  # 1
    ['Edu', 'Noah', 'Isra'],  # 2
]

print(lista_a[2][1])

enumeradas = enumerate(lista_a)
print(list(enumeradas))
print(enumeradas)

for va, vb in enumerate(lista_a, 53):  # enumerate pode começar de qualquer numero
    print(va, vb)

"""
[<---Enumerate

 0    1
(0, ['Igor', 'João', 'Gaby']), #0
(1, ['Maria', 'Aline', 'Michele']), #1
(2, ['Edu', 'Noah', 'Isra']) #2
]
"""
