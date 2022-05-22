from random import shuffle
p = input('Digite o nome do 1° aluno: ')
s = input('Digite o nome do 2° aluno: ')
t = input('Digite o nome do 3° aluno: ')
q = input('Digite o nome do 4° aluno: ')
lista = [p, s, t, q]
emb = shuffle(lista)
print('A ordem de apresentação dos alunos é: {}'.format(lista))