from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

game_images = [rock, paper, scissors]

score = [0, 0]
while True:
    user_choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    print(game_images[user_choice])

    computer_choice = randint(0, 2)

    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")

    elif user_choice == 0 and computer_choice == 2:
        score[0] += 1
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        score[1] += 1
        print("You lose")
    elif computer_choice > user_choice:
        score[1] += 1
        print("You lose")
    elif user_choice > computer_choice:
        score[0] += 1
        print("You win!")
    elif computer_choice == user_choice:
        score[0] += 1
        score[1] += 1
        print("It's a draw")

    print(f"Your score: {score[0]}")
    print(f"Computer's score: {score[1]}")

    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'n':
        break
