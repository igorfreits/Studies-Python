"""OS - Percorrendo arquivos e pastas"""
# Percorre os arquivos do sistema

import os

"""os.path.splitext()método em Python é usado para dividir o nome do
caminho em um par raiz e ext . Aqui, ext significa extensão e tem a
parte da extensão do caminho especificado, enquanto root é tudo, exceto a parte ext .
ext estará vazio se o caminho especificado não tiver nenhuma extensão.
Se o caminho especificado tiver um ponto inicial ('.'), Ele será ignorado."""

"""OS.walk() gera os nomes dos arquivos em uma árvore de diretórios percorrendo
a árvore de cima para baixo ou de baixo para cima.
Para cada diretório na árvore enraizada no diretório top (incluindo o próprio top),
ele produz uma 3-tupla (caminho de diretório, nomes de diretório, nomes de arquivo)."""

"""os.path.join()método em Python unir um ou mais componentes de caminho de forma inteligente.
Este método concatena vários componentes de caminho com exatamente
um separador de diretório ('/') após cada parte não vazia, exceto o último componente
de caminho. Se o último componente do caminho a ser unido estiver vazio,
um separador de diretório ('/') é colocado no final.
Se um componente do caminho representa um caminho absoluto,
todos os componentes anteriores unidos são descartados e a união continua a partir do componente do caminho absoluto."""

way = input('enter a path')  # digite um caminho/Inserir diretório
term_search = input('type a term')  # digite um termo/nome do arquivo


def format_size(size):
    base = 1024
    kilo = base
    mega = size ** 2
    giga = size ** 3
    tera = size ** 4
    peta = size ** 5

    if size < kilo:
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'K'
    elif size < tera:
        size /= giga
        text = 'K'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'
    size = round(size, 2)
    return f'{size}{text}'.replace('.', ',')


counter = 0  # contador
for root, directory, files in os.walk(way):
    for file in files:
        if term_search in file:
            try:
                counter += 1
                way_complete = os.path.join(root, file)  # caminho completo

                name_file, file_extension = os.path.splitext(
                    way_complete)  # Extensão do arquivo
                # Pega o tamanho do arquivo
                size = os.path.getsize(way_complete)

                print()
                print('found the file:', file)  # Encontrei o arquivo
                print('way:', way_complete)  # Caminho
                print('name:', name_file)
                print('formatted size', format_size(size))  # tamanho formatado
                print('extension:', file_extension)
            except PermissionError as e:
                print('without permission')  # sem permissão
            except FileNotFoundError as e:
                print('File not found')  # Arquivo nao encontrado
            except Exception as e:
                print('unknown error')  # erro desconhecido
print()
print(f'{counter} file(s) found')  # arquivo(s) encontrado
