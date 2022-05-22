from dataclasses import replace


def real(valor):
    return f'R${valor:.2f}'.replace('.', ',')
