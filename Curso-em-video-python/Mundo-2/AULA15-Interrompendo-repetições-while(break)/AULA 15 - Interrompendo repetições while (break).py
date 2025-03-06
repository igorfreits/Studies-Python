"""
Interrompendo repetições while (break)
"""
# break - Condição de parada

"""
enquanto Verdadeiro
    se "terra'
        passo
    se "vazio'
        pula
    se "moeda'
        pega
    se "troféu"
        pula
        interrompe
pega
"""

soma = 0
while True:  # laco infinito
    n = int(input('Digite um numero: '))
    if n == 999:  # So sera interrompido se o usuário digitar 999
        break  # Interrompe o laco
    soma += n
print(f'A soma vale {soma}')
