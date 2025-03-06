# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Escolha aleatoriamente uma palavra da lista_palavras e atribua-a a uma variável chamada palavra_escolhida.
palavra_escolhida = random.choice(word_list)


# TODO-2 - Peça ao usuário que adivinhe uma letra e atribua sua resposta a uma variável chamada guess.
# Faça adivinhar minúsculas.

guess = input("Adivinhe uma letra: ").lower()

# TODO-3 - Verifique se a letra que o usuário adivinhou (adivinhe) é uma das letras da palavra escolhida
for letra in palavra_escolhida:
    if letra == guess:
        print("Right")
    else:
        print("Wrong")

print(palavra_escolhida)
