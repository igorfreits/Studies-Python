"""
Filter()
"""
# Filtra coisas
from dados import pessoas, produtos, lista
"""
filter(function, iterable)
Constrói um iterador a partir dos elementos de iterable para
os quais function retorna verdadeiro. iterable pode ser uma sequência,
um contêiner que com suporte a iteração, ou um iterador. Se function for None,
a função identidade será usada, isto é,
todos os elementos de iterable que são falsos são removidos.

Note que filter(function, iterable) é equivalente a expressão geradora
(item for item in iterable if function(item))
se function não for None e
(item for item in iterable if item) se function for None.
"""
# Filter()
#                   Função()        Iterável
n1_lista = filter(lambda x: x > 5, lista)
print(list(n1_lista))  # Retorna verdadeiro ou falso
# Todo o elemento > 5 vai retornar True e ficara na nova_lista
# Os que retornarem False serão removiso da nova_lista
# Função filter recebe uma função() como primeiro argumento
# Não retorna uma lista pronta, retorna um iterador(converter)

# list Comprehension
n2_lista = [x for x in lista if lista if x > 5]
print(n2_lista)


def filtra(produto):
    # So ira retornar True se o valor for maior que 50
    # Os valores menos que 50 retornam  como NOne
    if produto['preço'] > 50:
        produto['e_caro'] = True
# Valores > 50 tera um novo dicionario
    return True


n3_produto = filter(filtra, produtos)
for produto in n3_produto:
    print(produto)


def idade(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


n4_lista = filter(idade, pessoas)

for pessoa in n4_lista:
    print(pessoa)
