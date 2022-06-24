"""Sys.argv - Executando arquivos com argumentos no sistema

1° - Passar o versão do python desejadas(windows: python "arquivo.py")
2° - Passar scrypt
"""
import sys
import os
arguments = sys.argv
qts_arguments = len(arguments)

if qts_arguments <= 1:
    print('missing arguments')
    print('-a', 'para listar ps arquivos nesse pasta', sep='\t')
    print('-d', 'para listar ps arquivos nesse pasta', sep='\t')
    sys.exit()

so_files = False
files = False
if '-a' in arguments:
    so_files = True

only_directories = False
if '-d' in arguments:
    only_directories = True

for file in os.listdir('.'):
    if so_files:
        if os.path.isfile(file):
            print(file)

    if only_directories:
        if os.path.isfile(file):
            print(file)
