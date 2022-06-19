"""
Comportamento de geradores e iteradores
"""
# Sequências  - tuples, list, str (Iteraveis

# Consomem os valores
nome = 'Igor Freitas'
iterador = iter(nome)
gerador = (letra for letra in nome)
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print()

for letra in gerador:
    print(letra)

for letra in gerador:
    print(letra)

for letra in nome:  # Next automatico no código
    print(letra)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
