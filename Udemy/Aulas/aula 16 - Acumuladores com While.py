"""
While / Else
contadores
acumuladores
"""

contador = 1  # conta de forma linear
acumulador = 1  # Acumula valores durante a execução do laço

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:  # o Else nao sera executado
        break

    acumulador = acumulador + contador

    contador += 1
else:
    print('Cheguei no Else')  # Quando o While for falso o Else sera executado
print('Isso sera executado')
