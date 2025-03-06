resposta = 'S'
media = soma = quantidade = maior = menor = 0

while resposta in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quantidade += 1
    resposta = input('Deseja continuar? [S]/[N]').upper().strip()[0]
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / quantidade
print(f'Voce digitou {quantidade} numeros e sua media foi de {media:.2f}')
print(f'O maior valor foi de {maior} e o menor valor foi de {menor}')
