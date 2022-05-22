string = '0123456789012345678901234567890123456789012345678901234567890123456789'

n = 10
contadores = [i for i in range(0, len(string), n)]
print(contadores)

tuplas = [(i, i + n) for i in range(0, len(string), n)]
print(tuplas)

lista = [string[i:i + n] for i in range(0, len(string), n)]
print(lista)

raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
print(raw)

retorno = '.'.join(lista)
print(retorno)
