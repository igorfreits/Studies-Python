"""Pillow: redimensionando várias imagens automaticamente

A Python Imaging Library (expansão do PIL) é o pacote de processamento de imagens
de fato para a linguagem Python. Ele incorpora ferramentas leves de processamento
de imagem que auxiliam na edição, criação e salvamento de imagens. O suporte para
Python Imaging Library foi descontinuado em 2011, mas um projeto chamado pillow
bifurcou o projeto PIL original e adicionou suporte Python3.x a ele.
O pillow foi anunciado como um substituto do PIL para uso futuro.
O Pillow oferece suporte a um grande número de formatos de arquivo de imagem,
incluindo BMP, PNG, JPEG e TIFF. A biblioteca incentiva a adição de suporte para
formatos mais novos na biblioteca, criando novos decodificadores de arquivo.


-https://pillow.readthedocs.io/en/stable/
-https://acervolima.com/python-pillow-um-garfo-de-pil/
"""

import os
from PIL import Image
# Também converte imagens dentro de subpastas


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):  # Verifica se o diretório existe
        raise NotADirectoryError(f'{main_images_folder} does not exist')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            convert_tag = '_CONVERTED'

            new_file = file_name + convert_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            # if convert_tag in full_path: #Remove os arquivos convertidos
            #     os.remove(full_path)
            #     print(f'converted {full_path} converted files were deleted')
            # continue

            if os.path.isfile(new_file_full_path):
                print(f'file {new_file_full_path} already exists')
                continue

            if convert_tag in full_path:
                print('image already converted')
                continue

            img_pillow = Image.open(full_path)

            width, height = img_pillow.size  # Tamanho das imagens
            # Regra de 3 pra descobrir o new_height
            new_height = round((new_width * height)/width)
            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS
            )  # Redimensiona a imagem

            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70
            )

            print(f'{full_path} successfully converted')
            new_image.close()
            img_pillow.close()
            # os.remove(full_path) #Remove os arquivos originais


"""os.path.splitext()método em Python é usado para dividir o nome do caminho em um
par raiz e ext"""


if __name__ == '__main__':
    main_images_folder = r'C:\Users\Igor\Desktop\Estudos\Programação em Python\Mundo-invertido\Files\image'
    main(main_images_folder, new_width=1920)
