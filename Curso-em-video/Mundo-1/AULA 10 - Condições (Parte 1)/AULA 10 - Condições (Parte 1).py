"""
Condições simples e compostas
"""

# Metodos contem ()

"""
carro.siga()
EX:
se carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão:
    carro.siga()
    carro.esquerda
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()
"""

# if carro.esquerda(): - if condição:
#   bloco True - condição caso for verdadeira (Sempre com tab para executar o if)
# else: - Se não
#   bloco False - condição se for falsa(sempre com tab para executar o  else

# Se tiver somente o if - condição simples
# Se tiver if e else - condição composta

tempo = int(input('Quantas anos tem o seu carro?: '))
print('carro novo'if tempo <= 3 else 'carro velho')  # condição simplificada(usar uma linha de codigo


if tempo <= 3:
    print('Carro novo')
else:
    print('carro velho')
print('--FIM--')

# so sera executado uma linha de codigo

nome = str(input('Qual o seu nome? '))
if nome == 'Igor':
    print('Seu nome é lindo!')
else:
    print('Seu nome é tão normal')
print(f'Bom dia, {nome}!')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))

media = n1 + n2 / 2
print(f'A sua media foi de {media:.2f}')
if media >= 6:
    print('PARABENS VOCE FOI APROVADO!')
else:
    print('INFELIZMENTE VOCE FOI REPROVADO! ESTUDO MAIS')