"""Context Manager - Criando e Usando gerenciadores de contexto(POO)"""
from contextlib import contextmanager


"""class File:
    def __init__(self, file, mode):
        print('opening file')  # Abrindo arquivo
        self.file = open(file, mode)

    def __enter__(self):
        print('returning file')  # Retornando arquivo
        return self.file

    def __exit__(self, exc_type, exc_value, trace):
        print('closing file')  # fechando arquivo
        self.file.close()
        # print(exc_type, exc_value, trace)
        # Tratei a exceção
        return True"""


@contextmanager
def opening(file, mode):
    try:
        file = open(file, mode)
        print('opening file')  # Abrindo arquivo
        yield file
    finally:
        print('closing file')  # fechando arquivo
        file.close()


with opening('abc.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
