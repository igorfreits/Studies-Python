"""
Criando, lendo, escrevendo e apagando arquivos

https://docs.python.org/pt-br/3/library/functions.html#open
"""
"""
'r' - abre para leitura (padrão)

'w' - abre para escrita, truncando o arquivo primeiro
(removendo tudo o que estiver contido no mesmo)

'x' - abre para criação exclusiva, falhando caso o arquivo exista

'a' - open for writing, appending to the end of file if it exists

'b' - binary mode

't' - modo texto (padrão)

'+' - aberto para atualização (leitura e escrita)
"""
try:
    import json
    import os
    # Abre um arquivo.txt para escrita(w) e para leitura e escrita(+)
    file = open('abc.txt', 'w+')  # Apaga todas aas linhas ao ser iniciado
    file.write('Linha 1\n')  # Escreve dentro o txt
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    # Localização do cursor (Volta pro inicio
    # (Também pode ser usado somente o zero pra voltar pro inicio)
    file.seek(0, 0)
    print(file.read())  # Exibi oque esta no txt

    print('######################')

    file.seek(0)  # Precisa voltar para o incio do código
    print(file.readline(), end='')  # le linha por linha
    print(file.readline(), end='')

    file.seek(0, 0)
    print(file.readlines())  # Exibi o txt em uma linha

    file.seek(0, 0)
    for linha in file:  # Itera sobre o txt
        print(linha, end='')

# Precisa fechar para encerrar
finally:  # Sempre sera executado, mesmo se conter erros
    file.close()

# with - Cria um arquivo e fecha automaticamente(Gerenciador de contexto)
# Melhor forma de trabalhar
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')  # File = variável
    file.write('Linha 2\n')

    file.seek(0)
    print(file.read())

# r = Exibi para leitura
with open('abc.txt', 'r') as file:
    print(file.read())

# Poe o cursor no final da linha e pode adicionar mais linhas
# a = Adiciona coisar sem precisar apagar
with open('abc.txt', 'a+') as file:
    # Cada vez que for executado ira adicionar um linha
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    print(file.read())

os.remove('abc.txt')  # apaga o arquivo

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Converte o arquivo para um dicionario

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
