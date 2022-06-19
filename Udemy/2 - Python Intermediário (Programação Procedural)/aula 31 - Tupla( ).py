"""
Tuplas()
"""

# semelhantes a listas [ ]
# TUPLAS SÂO IMUTÁVEIS

t1 = (1, 2, 3, 'Igor')  # tuple
print(type(t1))

t2 = ()  # Tupla vazia (Precisa de pelo menos dois itens)
print(type(t2))

print(t1[3])  # Acessar item especifico

for t in t1:  # Tuplas são iteráveis
    print(t)

print(t1[2:])  # Fatiamento

t3 = 1, 2, 'a'  # Não precisa de ( )
print(type(t2))

t4 = (1, 2, 3, 'Igor')
t5 = (4, 5, 6)
tt = t4 + t5  # Concatenação
print(tt)

n1, n2, n3, n4, *_ = tt
print(n4)  # Desempacota

t6 = (1, 2, 3) * 10  # Mostra a tupla t6 10vezes
print(t6)

t7 = (1, 2, 3, 4, 5)
t7 = list(t7)  # Converte um tupla em lista
print(t7)

t7[1] = 3000
t7 = tuple(t7)  # Converte um lista em tupla
print(t7)
