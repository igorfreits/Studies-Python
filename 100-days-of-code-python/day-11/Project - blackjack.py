############### Blackjack Project #####################

# Dificuldade Normal 😎: Use todas as Dicas abaixo para concluir o projeto.
# Dificuldade Difícil 🤔: Use apenas as Dicas 1, 2, 3 para concluir o projeto.
# Dificuldade Extra Difícil 😭: Use apenas as Dicas 1 e 2 para concluir o projeto.
# Especialista em Dificuldades 🤯: Use apenas a Dica 1 para concluir o projeto.

############### Our Blackjack House Rules #####################

# O baralho é ilimitado em tamanho.
# Não há curingas.
# O Valete/Rainha/Rei contam como 10.
# O Ás pode contar como 11 ou 1.
# Use a seguinte lista como o baralho de cartas:
import random
from art import logo
from replit import clear
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# As cartas da lista têm a mesma probabilidade de serem sorteadas.
# As cartas não são removidas do baralho à medida que são compradas.
# O computador é o revendedor.

##################### Hints #####################

# Dica 1: Acesse este site e experimente o jogo de Blackjack:
# https://games.washingtonpost.com/games/blackjack/
# Então experimente o projeto Blackjack completo aqui:
# http://blackjack-final.appbrewery.repl.run

# Dica 2: Leia este detalhamento dos requisitos do programa:
# http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Em seguida, tente criar seu próprio fluxograma para o programa.

# Dica 3: Baixe e leia este fluxograma que criei:
# https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Dica 4: Crie uma função deal_card() que use a Lista abaixo para *retornar* um cartão aleatório.
# 11 é o Ás.
#cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Dica 5: Dê ao usuário e ao computador 2 cartas cada usando deal_card() e append().
#user_cards = []
#computer_cards = []

# Dica 6: Crie uma função chamada calculate_score() que receba uma Lista de cartões como entrada
# e retorna a pontuação.
# Procure a função sum() para ajudá-lo a fazer isso.

# Dica 7: Dentro de calculate_score() verifique se há um blackjack (uma mão com apenas 2 cartas: ás + 10) e retorne 0 em vez da pontuação real. 0 representará um blackjack em nosso jogo.

# Dica 8: Dentro de calculate_score() verifique se há um 11 (ás). Se a pontuação já for superior a 21, remova o 11 e substitua-o por 1. Pode ser necessário procurar append() e remove().

# Dica 9: Chame calculate_score(). Se o computador ou o usuário tiver um blackjack (0) ou se a pontuação do usuário for superior a 21, o jogo termina.

# Dica 10: Caso o jogo não tenha terminado, pergunte ao usuário se ele deseja comprar outra carta. Se sim, use a função deal_card() para adicionar outro cartão à lista user_cards. Se não, então o jogo terminou.

# Dica 11: A pontuação deverá ser verificada novamente a cada nova carta retirada e as verificações da Dica 9 precisam ser repetidas até o final do jogo.

# Dica 12: Assim que o usuário terminar, é hora de deixar o computador jogar. O computador deve continuar tirando cartas enquanto tiver uma pontuação menor que 17.

# Dica 13: Crie uma função chamada compare() e passe o user_score e computer_score. Se o computador e o usuário tiverem a mesma pontuação, é um empate. Se o computador tiver um blackjack (0), o usuário perde. Se o usuário tiver um blackjack (0), então o usuário ganha. Se o user_score for superior a 21, o usuário perde. Se o computer_score for superior a 21, o computador perde. Se nenhuma das opções acima, então o jogador com a maior pontuação ganha.

# Dica 14: Pergunte ao usuário se ele deseja reiniciar o jogo. Se eles responderem sim, limpe o console e inicie um novo jogo de blackjack e mostre o logotipo do art.py.


def deal_card():
    return random.choice(cartas)


def calculate_score(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Empate 🙃"
    elif computer_score == 0:
        return "Perdeu, o computador tem um Blackjack 😱"
    elif user_score == 0:
        return "Ganhou com um Blackjack 😎"
    elif user_score > 21:
        return "Você perdeu 😭"
    elif computer_score > 21:
        return "Você ganhou 😁"
    elif user_score > computer_score:
        return "Você ganhou 😁"
    else:
        return "Você perdeu 😭"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  Sua cartas: {user_cards}, pontuação: {user_score}")
        print(f"  Cartas do computador: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Você quer mais uma carta? 'y' ou 'n': ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Sua cartas: {user_cards}, pontuação: {user_score}")
    print(
        f"  Cartas do computador: {computer_cards}, pontuação: {computer_score}")
    print(compare(user_score, computer_score))


while input("Você quer jogar um jogo de Blackjack? 'y' ou 'n': ") == "y":
    clear()
    play_game()
