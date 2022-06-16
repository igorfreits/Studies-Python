"""ZIP - Compactando / Descompactando arquivos"""
from zipfile import ZipFile
import os

""" Este módulo fornece ferramentas para:
criar, ler, escrever, adicionar, e listar um arquivo ZIP

-https://docs.python.org/pt-br/3/library/zipfile.html
"""
way = r'C:\Users\Igor\Desktop\Test'

# Cria um arquivo e colocar arquivos num zip
with ZipFile('file.zip', 'w') as zip:
    for file in os.listdir(way):
        full_path = os.path.join(way, file)
        zip.write(full_path, file)

with ZipFile('file.zip', 'r') as zip:  # Exibi os arquivos dentro no zip
    for file in zip.namelist():
        print(file)

with ZipFile('file.zip', 'r') as zip:  # Descompacta os arquivos do zip
    zip.extractall('unzipped')  # descompactado
