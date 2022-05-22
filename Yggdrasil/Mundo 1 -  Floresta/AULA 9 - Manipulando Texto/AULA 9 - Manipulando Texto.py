frase = 'Curso em Vídeo Python'  # 21 caracteres incluindo espaços

# fatiamento
print(frase[9:21:2])
# [inicio do fatiamento:fim do fatiamento:pula caractere] um a menos no final

print(frase[:5])  # do 0 ate o 4
print(frase[15:])  # do 15 ate final
print(frase[9::3])  # do 9 ate final pulando de 3 em 3 casas

# analise
print(len(frase))  # len() - mostra quantidade de caracteres = 21
print(frase.count('o'))  # .count() - mostra quantidade de X caracteres = 3
print(frase.count('o', 0, 13))  # mostra quantidade de o entre 0 ate o 13 = 1
print(frase.find('deo'))  # .find() posicao de onde começou
print(frase.find('Android'))  # Mostra -1 pois nao existe esse texto

print('Curso' in frase)  # procura X frase "EM" na string

# Tranformação
print(frase.replace('Python', 'Android'))  # .replace() - substitui X po Y
print(frase.upper())  # .upper() - Deixa tudo em MAIÚSCULOS
print(frase.lower())  # .lower() - Deixa tudo em minusculo
print(frase.capitalize())  # .capitaliza() - Deixa a primeira letra na frase em Maiúsculo
print(frase.title())  # .title() - Deixa a primeira palavra da frase em Maiúsculo

frase1 = '   Aprenda Python  '
print(frase1.strip())  # strip() - remove espaços da borda
print(frase1.rstrip())  # rstrip() - remove espaços da direita
print(frase1.lstrip())  # lstrip() - remove espaços da esquerda

# Divisão

print(frase.split())  # .split() - cada palavra recebe um lsita com base nos espaços

# Junção
print('_'.join(frase))  # " ".join() - substitui espaços por X para cada letra

