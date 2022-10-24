# Number Guessing Game Objectives:

# Inclua um logotipo de arte ASCII.
# Permitir que o jogador envie um palpite para um número entre 1 e 100.
# Verifica o palpite do usuário em relação à resposta real. Imprima "Muito alto". ou "Muito baixo". dependendo da resposta do usuário.
# Se eles acertaram a resposta, mostre a resposta real ao jogador.
# Acompanhe o número de voltas restantes.
# Se eles ficarem sem turnos, forneça feedback ao jogador.
# Inclua dois níveis de dificuldade diferentes (por exemplo, 10 palpites no modo fácil, apenas 5 palpites no modo difícil).

from art import logo
import random


def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("Estou pensando em um número entre 1 e 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    number = random.randint(1, 100)
    print(f"Você tem {attempts} tentativas restantes para adivinhar o número.")
    guess = int(input("Make a guess: "))
    while guess != number:
        if guess > number:
            print("Muito alto.")
            attempts -= 1
            print("Tente novamente.")
        else:
            print("Muito baixo.")
            attempts -= 1
            print("Tente novamente.")
        if attempts == 0:
            print("Você ficou sem palpites, você perdeu.")
            break
        print(
            f"Você tem {attempts} tentativas restantes para adivinhar o número.")
        guess = int(input("Adivinhe:"))
    if guess == number:
        print(f"Você acertou! A resposta foi {number}.")
