"""OS + SHUTIL - Mover, copiar e apagar arquivos"""
import os
import shutil

original_path = r'C:\Users\Igor\Desktop\Estudos\Gestão deTI'  # Pasta original
new_way = r'C:\Users\Igor\Desktop\Estudos\Gestão deTI\serie2'  # nova pasta

"""os.mkdir()método em Python é usado para criar um diretório denominado path
com o modo numérico especificado. Este método levanta FileExistsError se o
diretório a ser criado já existe."""

"""shutil.move()método Move recursivamente um arquivo ou diretório(origem)
para outro local (destino) e retorna o destino. Se o diretório de destino já existe,
src é movido para dentro desse diretório. Se o destino já existe, mas não é um diretório,
ele pode ser substituído, dependendo da os.rename()semântica"""

"""O método shutil.copy() em Python é usado para copiar o conteúdo do arquivo de
origem para o arquivo ou diretório de destino . Ele também preserva o modo de permissão do arquivo,
mas outros metadados do arquivo, como os horários de criação e modificação do arquivo,
não são preservados."""
try:
    os.mkdir(new_way)  # Cria um diretório
except FileExistsError as e:
    print(f'folder {new_way}  already exists')

# Para copiar insira o "original_path"
for root, dirs, files in os.walk(new_way):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_way, file)
        # if '.pdf' in file:
        #     shutil.copy(old_file_path, new_file_path)  # copia arquivos
        #     print(f'file {file} copied successfully!')
        if '.pdf' in file:
            os.remove(new_file_path)
            print(f'file {file} deleted successfully')
