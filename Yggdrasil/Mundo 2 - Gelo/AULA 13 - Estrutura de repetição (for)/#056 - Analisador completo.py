soma_idade = 0
media_idade = 0

maior_idade_homem = 0
nome_velho = 0

total_mulher20 = 0

for c in range(1, 5):
    print(f'-----{c}ª Pessoa-----')
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    sexo = input('SEXO [M/F]: ').strip()

    soma_idade += idade

    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        total_mulher20 += 1

media_idade = soma_idade / 4
print(f'A media de idade do grupo e de {media_idade:.2f} anos')
print(
    f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}')
print(f'Ao todo sao {total_mulher20} mulheres com menos de 20 anos')
