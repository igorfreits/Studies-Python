soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        contador += 1
print(f'Voce digitou {contador} PARES e a soma foi de {soma}')
