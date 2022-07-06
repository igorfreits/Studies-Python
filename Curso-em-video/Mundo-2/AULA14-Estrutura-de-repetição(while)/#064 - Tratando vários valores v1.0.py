n = contador = soma = 0
n = int(input('Digite um numero [999 parar parar]: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um numero [999 parar parar]: '))
print(f'Voce digitou {contador} números e a soma entre eles foi de {soma}')
