n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2} a media do aluno sera: {media}')

if media < 5:
    print('REPROVADO')

elif media >= 7:
    print('APROVADO')

elif media >= 5 and media < 7: # ou apenas else:
    print('RECUPERAÇÃO')

