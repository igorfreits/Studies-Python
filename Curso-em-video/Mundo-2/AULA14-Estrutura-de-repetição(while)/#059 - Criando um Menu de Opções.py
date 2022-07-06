n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
opção = 0

while opção != 5:
    print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa""")
    opção = int(input('Qual sua opção? '))

    if opção == 1:
        soma = n1+n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valoré {maior}')
    elif opção == 4:
        print('Informe os novos numeros... ')
        n1 = int(input('Digite um numero:'))
        n2 = int(input('Digite outro numero:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa. Volte sempre!')
