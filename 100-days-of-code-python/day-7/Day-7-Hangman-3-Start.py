# Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use um loop while para deixar o usuário adivinhar novamente.
# O loop só deve parar quando o usuário adivinhar todas as letras da palavra
# escolhida e 'display' não tiver mais espaços em branco ("_"). Então você pode dizer ao usuário que eles ganharam.
while True:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Posição atual: {position}\n Letra atual: {letter}\n Letra adivinhada: {guess}")
        print(display)
        if letter == guess:
            display[position] = letter
    if "_" not in display:
        print("You win")
        break
print(display)
