from turtle import Turtle, Screen
import random


is_race_on = False
# Tela
screen = Screen()

# Tamanho da tela
screen.setup(width=700, height=350)


# Titulo da tela
screen.title("Aposta em tartarugas ninja")


# pop-up para apostar
user_bet = screen.textinput(
    title="Faça sua aposta",
    prompt="Em qual tartaruga ninja você aposta?")


tartarugas = {'Raphael': 'red', 'Leonardo': 'blue',
              'Michelangelo': 'orange', 'Donatello': 'purple',
              'Splinter': 'black', 'Destruidor': 'gray'}

all_turtles = []

y_positions = [-100, -50, 0, 50, 100, 150]

# Tartarugas
for turtle in tartarugas:
    # Cria uma nova tartaruga
    new_turtle = Turtle(shape="turtle")
    # Cor da tartaruga
    new_turtle.color(tartarugas[turtle])
    # Apaga o rastro da tartaruga
    new_turtle.penup()
    # Cordendas iniciais
    new_turtle.goto(x=-335, y=y_positions[0])
    # Adiciona a tartaruga na lista
    all_turtles.append(new_turtle)
    # Remove a primeira posição da lista
    y_positions.pop(0)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()

            for name, color in tartarugas.items():
                if winning_color == user_bet:
                    if color == winning_color:
                        print(f"Você ganhou! O {name} venceu!")
                else:
                    if color == winning_color:
                        print(f"Você perdeu! O {name} venceu!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
