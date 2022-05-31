"""Agregação  (POO)"""
from cartclass import CartValue, Produto
# Relação de agregação
"""
Se relaciona com outra classe ou seja vai estar associada a outra classe.
Mas usa e depende do código de outra classe"""

# Carro existe sem as rodas e as rodas existem sem o carro
# Porem o carro nao funciona sem as rodas

carrinho = CartValue()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.insert_product(p1)
carrinho.insert_product(p2)
carrinho.insert_product(p3)
carrinho.insert_product(p1)
carrinho.insert_product(p1)
carrinho.insert_product(p2)
carrinho.insert_product(p3)

carrinho.list_products()
print(carrinho.soma_total())
