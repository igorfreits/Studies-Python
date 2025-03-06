# Step 5

import Hangman_art
import Hangman_world
import random
# TODO-1: - Atualize a lista de palavras para usar a 'word_list' de hangman_words.py
# Exclua esta linha: word_list = ["ardvark", "baboon", "camel"]chosen_word = random.choice(word_list)
# TODO-2: - Importe os estágios do hangman_art.py e faça com que este erro desapareça.
word_list = Hangman_world.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Importe o logotipo do hangman_art.py e imprima-o no início do jogo.
# Testing code
print(f'Pssst, a palavra secreta é {chosen_word}.')
print(Hangman_art.logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

# TODO-4: - Se o usuário digitou uma letra que já adivinhou, imprima a letra e avise.
# Check guessed letter

    if guess in display:
        print(f'Você já tentou a letra {guess}. Tente outra letra.')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - Se o usuário não adivinhou a letra e a letra não está na palavra, perca uma vida.
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

# TODO-2: - Importe os estágios do hangman_art.py e faça com que este erro desapareça.
    print(Hangman_art.stages[lives])
