"""
For in em Python
Iterando strings com for
Função range (start=0, stop, step=1)
"""

# While para valores infinitos
# For para valores finitos

texto = 'Python'  # String finita

c = 0
while c < len(texto):
    print(texto[c])
    c += 1

for letra in texto:  # Para condição : -  for condição: Não precisa de contador igual ao while
    print(letra)

for n, letra in enumerate(texto):  # Enumera a cada volta do laço for
    print(n, letra)

print('#####')

# Laço for nao precisa de contador ou pode usar a função enumerate()

for n in range(10):  # Mostra de 0 a 9
    print(n)

# variavel nao precisa existir antes

"""Função range recebe 3 parametro/argumentos
(start=0, stop, step=1) valores padroes
(inicio, termina, pula casas)"""

# nao depende do laço for e nem o laço for depende do range

for n in range(20, 10):  # não mostra nada na tela por que o inicio é maior que o fim
    print(n)

print('#####')

for n in range(20, 10, -1):  # decrementa o valor inicial indo do 20 ate o 11
    print(n)

# Mostra um digito a mais

print('#####')

for n in range(0, 10, 2):  # Começa do 0 e vai ate o 10 pulando de 2 em 2
    print(n)

print('#####')

for n in range(0, 100, 8):  # mostra valores múltiplos de 8
    print(n)

print('#####')

for n in range(100):  # Também pode ser usado para mostrar múltiplos de 8
    if n % 8 == 0:
        print(n)

print('#####')

# continue - pula para o proximo laço
# break - termina o laço

nova_string = ' '

for letra in texto:
    if letra == 't':
        continue  # Não tera a letra 't'
        nova_string = nova_string.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break  # Ira parar na letra 'h'
    else:
        nova_string += letra
print(nova_string)
