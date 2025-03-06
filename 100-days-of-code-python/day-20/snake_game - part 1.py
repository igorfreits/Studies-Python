from turtle import Screen
from time import sleep
from snake import Snake

tela = Screen()
tela.setup(width=600, height=600)

# cor de fundo
tela.bgcolor("black")

# titulo da tela
tela.title("Jogo da Cobrinha")

# velocidade da animação
tela.tracer(0)

# cria a cobra
cobra = Snake()

# controla o jogo
tela.listen()
tela.onkey(cobra.up, "Up")
tela.onkey(cobra.down, "Down")
tela.onkey(cobra.left, "Left")
tela.onkey(cobra.right, "Right")

game_is_on = True

while True:
    # atualiza a tela
    tela.update()
    sleep(0.1)
    cobra.move()