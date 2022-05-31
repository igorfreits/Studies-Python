""" Composição(POO)"""
from clientclass import Client
# Relação de composição
"""Composição, uma classe usa, depende e mantém uma referencia da outra classe
(se a classe principal morre, as filhas também morrem)"""

"""Se a classe principal for apagada todos os objetos
que a classe principal utilizou vão ser apagados com ela"""

client1 = Client('Igor', 23)
client1.insert_address('Portugal', 'PT')
print(client1.name)
client1.list_address()
del client1

print()

client2 = Client('Michele', 21)
client2.insert_address('São Paulo', 'SP')
client2.insert_address('Rio de Janeiro', 'RJ')
print(client2.name)
client2.list_address()
del client2

print()

client3 = Client('Noah', 15)
client3.insert_address('Belo Horizonte', 'MG')
print(client3.name)
client3.list_address()
del client3

print('#'*100)
