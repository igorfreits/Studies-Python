from replit import clear
from art import logo

# Dica: Você pode chamar clear() para limpar a saída no console
print(logo)
print('Bem-vindo ao leilão secreto.')

apostas = {}
continuar = True

while continuar:
    nome = input("Qual é o seu nome? ")
    valor = int(input("Qual é o seu lance? R$"))
    apostas[nome] = valor
    continuar = input(
        'Existem outras pessoas para apostar? Digite "sim" ou "não"').lower() == "sim"
    clear()

maior = 0
vencedor = ""

for nome in apostas:
    valor = apostas[nome]
    if valor > maior:
        maior = valor
        vencedor = nome

print(f'O vencedor é {vencedor} com um lance de ${maior}.')
