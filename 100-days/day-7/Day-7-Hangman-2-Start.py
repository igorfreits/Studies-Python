# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Cria uma lista vazia chamada display.
# Para cada letra na palavra_escolhida, adicione um "_" a 'exibir'.
# Então, se a palavra escolhida for "maçã",
# a exibição deve ser ["_", "_", "_", "_", "_"] com 5 "_" representando cada letra a ser adivinhada
guess = input("Guess a letter: ").lower()
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"


# TODO-2: - Percorrer cada posição na palavra escolhida;
# Se a letra nessa posição corresponder a 'adivinha', revele essa letra no visor nessa posição.
# por exemplo. Se o usuário adivinhou "p" e a palavra escolhida foi "maçã",
# então a exibição deve ser ["_", "p", "p", "_", "_"].
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        print("Right")
        display[position] = letter
        

    else:
        print("Wrong")


# TODO-3: - Imprima 'display' e você deverá ver a letra adivinhada na posição correta e todas as outras letras substituídas por "_".
# Dica - Não se preocupe em fazer o usuário adivinhar a próxima letra. Vamos resolver isso na etapa 3.

print(display)
