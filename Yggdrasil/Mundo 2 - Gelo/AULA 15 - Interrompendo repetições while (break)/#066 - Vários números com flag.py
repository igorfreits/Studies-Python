contador = soma = 0
while True:
    n = int(input('Digite um numero [999 para para]: '))
    if n == 999:  # flag - (condição de parada)
        break
    contador += 1
    soma += n
print(f'Voce digitou {contador} números e a soma do valores foi de {soma}')
