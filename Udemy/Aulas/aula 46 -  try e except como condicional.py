"""
try e except como condicional
"""


def converte_numero(valor):  # Similar ao if e else
    try:
        valor = int(valor)  # Ira tentar executar
        return valor
    except ValueError:
        try:
            valor = float(valor)  # Se nao conseguir executar(ira tentar esse)

            return valor
        except ValueError:
            pass


while True:
    # Input sempre retorna uma "String"
    numero = converte_numero(input('Digite um numero: '))
    if numero is None:
        print('Isso não é um numero')
    else:
        print(numero * 2)
