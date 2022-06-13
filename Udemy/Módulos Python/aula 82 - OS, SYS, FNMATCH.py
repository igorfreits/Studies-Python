"""OS, SYS, FNMATCH - Convertendo vídeos com Python + FFMPEG"""

import sys
import fnmatch
import os
"https://ffmpeg.org/download.html"  # Site de download
"https://ffmpeg.org/documentation.html"  # Documentation

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

        output_file = f'{command_ffmpeg}/{name_file}_new{file_extension}'

        command = f' {command_ffmpeg} -i ""{full_path}" {input_legend}'
        f'{codec_video}{code_audio}{crf}{preset}{bitrate_audio}{debug}{output_file}'

        os.system(command)

