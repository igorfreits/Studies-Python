"""
While - Estrutura de repetição infinita
"""

# Laço com teste lógico

"""
while not "maça":

enquanto nao "maça":  # Enquanto for verdadeiro ira rodar o laço
    se "chão"
        passo
    se "vazio"
        passo
    se "moeda"
        pega
pega    

"""

contador = 1  # Enquanto o contador for menor que 10
while contador < 10:
    print(contador)
    contador += 1
print('FIM')

n = 1  # Ira rodar ate o valor 0 for digitado
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'  # Ira rodar ate r receber o valor 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input(' Quer continuar? [S/N]')).upper()
print('FIM')

n = 1
par = ímpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        ímpar += 1
print(f'Você digitou {par} PARES e {ímpar} ÍMPARES')
