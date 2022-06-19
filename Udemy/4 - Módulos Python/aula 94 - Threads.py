"""Threads - Executando processamentos em paralelo"""
from concurrent.futures import thread
from threading import Thread
from time import sleep
from threading import Lock
from tkinter import W

"""Threads são uma forma de fazer com que a sua aplicação execute tarefas de forma assíncrona,
por exemplo, enquanto uma estrutura de repetição é executada você pode executar uma outra rotina.

-Executa multitarefas no scrypt ao invés de executar de forma linear

-https://docs.python.org/pt-br/3.7/library/_thread.html
"""

"""# Forma linear
print('Hello')  # 1°
for i in range(5):  # 2°
    print(i)
print('world')  # 3°
print('##############')


class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


# Serão executados no meio do laço for
t1 = MyThread('Thread 1', 5)
t1.start()

t2 = MyThread('Thread 2', 3)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)"""


def to_take_time1(text, time):  # demorar
    sleep(time)
    print(text)


t1 = Thread(target=to_take_time1, args=('Hello World 1', 5))
t1.start()

t2 = Thread(target=to_take_time1, args=('Hello World 2', 1))
t2.start()

t2 = Thread(target=to_take_time1, args=('Hello World 3', 2))
t2.start()

for i in range(10):
    print(i)
    sleep(.5)

print('########')


def to_take_time2(text, time):  # demorar
    sleep(time)
    print(text)


t4 = Thread(target=to_take_time2, args=('Hello World 4', 5))
t4.start()

while t4.is_alive():  # Enquanto a thread nao for executada
    print('waiting for the thread')  # Esperando a thread
    sleep(2)

t4.join()  # Vai se juntar a thread principal
print('the thread is over')  # A thread acabou
"""O .join simplesmente pausa a thread atual (de onde ele foi chamado)
até que a thread alvo (a thread a que ele está atrelado) termine.

É uma forma de voltar a sincronizar o programa,
garantindo que não estejam ocorrendo processamentos em paralelo."""


class Ticket:
    def __init__(self, inventory):
        self.inventory = inventory
        self.lock = Lock()

    def purchase(self, inventory):
        self.lock.acquire()  # Evita que varias pessoas tentam comprar o ingresso(Tranca)

        if self.inventory < inventory:
            # não temos ingresso suficientes
            print("we don't have enough tickets")
            self.lock.release()
            return

        """Sem o Lock() varias pessoas irão comprar o ingresso ao mesmo tempo,
        fazendo que retorne valores negativos"""
        sleep(1)

        self.inventory -= inventory
        print(
            f'you bought {inventory} ticket(s). we still have {self.inventory} in inventory')
        self.lock.release()  # libera a chave


if __name__ == '__main__':
    tickets = Ticket(10)

    threads = []
    for i in range(1, 20):
        t5 = Thread(target=tickets.purchase, args=(i,))
        threads.append(t5)
    for t5 in threads:
        t5.start()

    running = True
    while running:
        running = False

        for t5 in threads:
            if t5.is_alive():
                running = True
                break
    print(tickets.inventory)
