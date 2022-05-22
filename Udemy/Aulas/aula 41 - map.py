"""
map
"""
# Mapeamento
# A função Map pega uma lista e a transforma numa nova lista,
# executando algum tipo de operação em cada elemento
# Importa dados de um outro arquivo .py
from dados import produtos, pessoas, lista

"""
map(function, iterable, ...)
Devolve um iterador que aplica function para cada item de iterable,
gerando os resultados.
Se argumentos iterable adicionais são passados,
function deve ter a mesma quantidade
de argumentos e ela é aplicada aos itens de todos os iteráveis em paralelo.
Com múltiplos iteráveis,
o iterador para quando o iterador mais curto é encontrado.
Para casos onde os parâmetros de entrada da função
já estão organizados em tuplas
"""

print(lista)

# map()
#               Função()         Iterável
nova_lista = map(lambda x: x * 2, lista)  # lambda função anonima
print(list(nova_lista))
# Função map recebe uma função() como primeiro argumento
# Não retorna uma lista pronta, retorna um iterador(converter)

print()

# list Comprehension
comprehension = [x * 2 for x in lista]
print(comprehension)

print()

for produto in produtos:  # Dicionario
    print(produto)


def imposto(p):  # Acessa a chave preço e altera o valor de preço
    p['preço'] = round(p['preço'] * 1.05, 2)  # round - max de casa decimais
    return p


# map esta mapeando um função que passa em cada elemento do meu iterável
novos_produtos = map(imposto, produtos)
print(novos_produtos)

for produto in novos_produtos:  # Esta acessando a coluna preço no dicionario
    print(produto)


def aumento_idade(p):
    # Nova chave criada dentro do dicionario
    p['nova_idade'] = round(p['idade'] * 1.20, 2)
    return p


nomes = map(aumento_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
