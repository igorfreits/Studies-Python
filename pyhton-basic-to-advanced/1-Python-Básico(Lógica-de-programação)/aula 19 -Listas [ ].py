"""
Listas em Python
fatiamento
append, insert, opo, del, clear, extend, + 
min,  mas
range"""

texto = 'Valor'
lst = [1, 2, 3, 4, 'Igor Freitas', True, 1.6]
# Listas podem receber vários tipos de valores, e devem conter []

#         0    1    2    3    4   + positivos
lista = ['A', 'B', 'C', 'D', 'E']
#         5    4    3    2    1   - negativos

lista[4] = 'Z'  # muda um determinado valor da lista

print(lista[0:3])  # listas podem ser fatiadas como as strings
print(lista[4])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

# extend = Estende os valores juntando as listas ou adiconando um novo item
l1.extend('K')
print(l1)

l2.append('B')  # Insere um novo valor no final da lista
print(l2)

l3 = [l1 + l2]  # Junta os valores da lista
print(l3)

# Adiciona um valor na lista a onde desejar (posição, Valor)
l2.insert(0, 'Banana')
print(l2)

l2.pop()  # Remove o ultimo valor da lista
print(l2)

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
del(l4[3:5])  # Exclui os valores selecionado (O ultimo nao é incluído)
print(l4)

print(max(l4))  # Mostra o maior valor
print(min(l4))  # Mostra o menor valor

l5 = list(range(1, 10))  # Cria uma lista com range()
print(l5)

soma = 0
for valor in l5:
    print(valor)
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')
print(soma)

l6 = ['String', True, 10, -20.7]

for elem in l6:
    print(f'O tipo de {elem} é {type(elem)}')

l7 = [4, 3, 2, 1]
print(sorted(l7))  # sorted() - organiza minha lista, mas nao altera ela

l7.sort()  # sort() Altera e organiza minha lista
print(l7)

l8 = [5, 7, 1, 2]
print(sorted(l8))
print(sorted(l8, reverse=True))  # reverse=True - Organiza em ordem reversa

lista_compras = ['banana', 'laranja', 'manga']  # [0,1,2]

lista_sonhos = []

# Pega informação de uma lista e joga na variável
sonho = lista_compras.pop(-1)

# .pop() apaga o ultimo  objeto da lista

print(sonho)

lista_sonhos.append(sonho)  # adiciona o item da variável na lista

print(lista_sonhos)

# tarefas
tarefas = []

tarefa = input('Insira uma tarefa: ')

tarefas.append(tarefa)
print(tarefas)

while tarefa != '':
    tarefa = input('Insira uma tarefa: ')
    tarefas.append(tarefa)
print(tarefas)
