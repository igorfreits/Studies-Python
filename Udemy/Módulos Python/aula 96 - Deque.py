"""Deque - Trabalhando com LIFO e FIFO

Pilha (stack) - LIFO - last in, first out
    Example: Pilha de livro que são adicionados um sobre o outra

Fila (queue) - FIFO - first in, first out
    Example: Uma fila de banco(ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os indices serão modificados
"""
from collections import deque
from time import sleep
# Metodos parecidos com list()
#
# Pilha(stack)
books = list()
books.append('Book 1')  # 1
books.append('Book 2')  # 2
books.append('Book 3')  # 3
books.append('Book 4')  # 4
books.append('Book 5')  # 5

book_remove = books.pop()  # 5
book_remove = books.pop()  # 4
book_remove = books.pop()  # 3
book_remove = books.pop()  # 2
book_remove = books.pop()  # 1
print(books, book_remove)

print('#################')

# Fila(queue)
row1 = deque()
row1.append('Igor')
row1.append('Michele')
row1.append('Noah')
row1.append('Alice')

print(f'{row1.popleft()} left')  # Remove o primeiro item da lista
print(f'{row1.popleft()} left')
print(f'{row1.popleft()} left')
print(f'{row1.popleft()} left')

# Defini o limite da lista(Remove o elemento mais antigo caso tente adicionar)
row2 = deque(maxlen=5)
row2.extend([1, 2, 3, 4])
row2.append(5)
row2.append(6)
print(row2),

# row3  = deque(maxlen=10)
# for i in range(100):
#     row3.append(i)
#     sleep(1)
#     print(row3)

row4 = deque()
row4.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
row4.rotate(3)  # coloca os valores finais ni inicio
print(row4)
