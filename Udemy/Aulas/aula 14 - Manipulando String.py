"""
Manipulando String
-String indices
-Fatiamento de strings[inicio:fim:passo
-função built-in len, abs, type, print, etc ...
Essas funções podem ser usadas diretamente em cada tipo

"https://docs.python.org/pt-br/3/library/functions.html"
"https://docs.python.org/pt-br/3/library/stdtypes.html"
"""
#       [012345678] - positivos
texto = 'Python_s2'  # casa numero no [] representa uma letra, inclui os espaços
#       [987654321] - negativos com sinal - dentro do[] EX [-9]

print(texto[2])  # mostra apenas o caractere selecionado

nova_string = texto[2:8:2]
# [inicio do fatiamento:fim do fatiamento:pula caracteres] colocar um numero a mais no fim do fatiamento

print(nova_string)

print(len(texto))  # conta os caracteres

for letra in texto:
    print(letra)
