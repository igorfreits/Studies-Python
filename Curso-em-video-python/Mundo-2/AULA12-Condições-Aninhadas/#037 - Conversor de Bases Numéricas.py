n = int(input('Digite um numero inteiro: '))

print('''Escolha um das basses para conversão
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Conveter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{n} convertido para BINARIO é: {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para OCTAL é: {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para HEXADECIMAL é: {hex(n)[2:]}')
else:
    print('Opção Invalida')
