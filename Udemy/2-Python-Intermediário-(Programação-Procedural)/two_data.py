from dataclasses import replace

# aula 48.2
# one_data

def real(valor):
    return f'R${valor:.2f}'.replace('.', ',')
