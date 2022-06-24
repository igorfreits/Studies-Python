"""OS, SYS, FNMATCH - Convertendo vídeos com Python + FFMPEG"""

import sys
import fnmatch
import os


"""O ffmpeg serve para conversão de vídeo com uma enormidade de codecs
-https://ffmpeg.org/download.html"  # Site de download
-https://ffmpeg.org/documentation.html"  # Documentation"""

"""fnmatch é usado para combinar curingas no estilo shell do Unix.
fnmatch() compara um único nome de arquivo com um padrão e retorna VERDADEIRO
se eles corresponderem, caso contrário, retorna FALSO.
A comparação diferencia maiúsculas de minúsculas quando o sistema operacional
usa um sistema de arquivos com distinção entre maiúsculas e minúsculas.
Os caracteres especiais e suas funções usados ​​em curingas no estilo shell são:

'*' - corresponde a tudo
'?' - corresponde a qualquer caractere único
'[seq]' - corresponde a qualquer caractere na seq
'[! seq]' - corresponde a qualquer caractere que não esteja em seq
Os metacaracteres devem ser colocados entre colchetes para uma correspondência literal.
Por exemplo, '[?]' Corresponde ao caractere '?'"""

"""O módulo sys fornece funções e variáveis ​​usadas para manipular diferentes
partes do ambiente de tempo de execução do Python e apesar de serem
completamente diferentes, muitas pessoas confundem o módulo sys e o módulo os
(módulo para manipular o sistema operacional).

Com o módulo sys você pode por exemplo, saber qual a plataforma do dispositivo
que está rodando o seu código, obter os caminhos de sistema que o interpretador
Python utiliza, módulos importados, versão do Python, entre outros.

-https://docs.python.org/pt-br/3/library/sys.html
"""

"""
ffmpeg -i
"Entrada" -1
"Legenda" -c
libx264
-crf 23
-preset
ultrafast
-c:a
aac
-b:a 320k
(-c:s srt -map v:0 a -map 1:0 -ss 00:00:00 -to 00:00:10 "Saida" #Video, audios, legendas
"""


if sys.platform == "win32":
    command_ffmpeg = "ffmpeg"

codec_video = '-c:v libx264'
crf = '-crf 23'  # video quality
preset = '-prest ultrafast'  # Tempo de conversão
code_audio = '=c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00:00 to 00:00:10'

original_path = ''  # Caminho original
destination_path = ''  # Caminho de destino

for root, folders, files in os.walk(original_path):
    for file in files:
        if not fnmatch.fnmatch(file, '*mkv'):  # formato dos videos
            continue
        full_path = os.path.join(root, file)  # caminho completo
        name_file, file_extension = os.path.splitext(full_path)
        subtitle_path = name_file + '.srt'

        if os.path.exists(subtitle_path):
            input_legend = f'-i "{subtitle_path}"'
            map_legend = '-c:s str -map v:0 -map a -map 1:0'
        else:
            input_legend = ''
            map_legend = ''
        name_file, file_extension = os.path.splitext(file)

        # Salva na mesma pasta, mas renomeia o arquivo
        new_file_name = name_file + '_new' + file_extension
        output_file = os.path.join(root, name_file)

        command = f' {command_ffmpeg} -i ""{full_path}" {input_legend}'
        f'{codec_video}{code_audio}{crf}{preset}{bitrate_audio}{debug}{output_file}'

        os.system(command)
