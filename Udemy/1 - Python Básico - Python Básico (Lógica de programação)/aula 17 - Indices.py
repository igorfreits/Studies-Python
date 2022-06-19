# Indices
#        0123456789.......................33
frase = 'O rato roeu a roupa do rei de Roma'  # Iterável

# Iterar = Passar por cada elemento - Se  tiver indice pode ser iterável

tamanho_frase = len(frase)  # 34 elementos contando com o zero

contador = 0
# Não é pode alterar a string atual, mas é possível copiar

nova_string = ' '

input_usuario = input('Qual letra você deseja colocar maiscula? ')

# Selecionar e apertar ctrl + / comenta a seleção

# Iteração <- Iterar = Ato de percorrer cada elemento da string
while contador < tamanho_frase:
    letra = frase[contador]

    if letra == input_usuario:
        # Converte a Letra escolhida para maiscula, mas so altera letra nao frase
        nova_string += input_usuario.upper()
    else:
        nova_string += letra

    """if letra == 'r':  # Altera a nova_string
        nova_string += 'R'
    else:
        nova_string += letra

    # print(frase[contador], contador)  # Mostra o indice de cada letra da variavel frase
    nova_string += frase[contador]
    print(nova_string)  # Forma a frase na sua tela ate mostrar toda a variavel frase"""
    contador += 1
print(nova_string)
