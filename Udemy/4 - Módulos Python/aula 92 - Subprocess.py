"""Subprocess - Executando programas e comandos externos"""

"""Executa programas externos e le suas saídas em seu código Python.
-O módulo subprocess permite que você crie novos processos,
conecte-se aos seus canais de entrada/saída/erro e obtenha seus códigos de retorno

-https://docs.python.org/pt-br/dev/library/subprocess.html
"""


# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

import subprocess
proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True, text=True  # A Saida do comando ira para variável
)  # Deve receber os argumentos

# print(proc.stderr)  # Caso tenha dado algum erro
# print(proc.stdout)  # Saida(monitoramento)
# print(proc.returncode)  # Retorna 0 quando o comando e executado com sucesso
# print(proc.args)  # argumentos

exit = proc.stdout
exit = exit.replace('tempo', 'Igor')
print(exit)
