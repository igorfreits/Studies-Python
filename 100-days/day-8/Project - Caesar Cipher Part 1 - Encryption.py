alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    'Digite "encode" para criptografar, digite "decode" para descriptografar:\n')
text = input('Digite seu texto:\n').lower()
shift = int(input('Digite o deslocamento:\n'))

# TODO-1: Criar uma função chamada 'encrypt' que recebe o 'text' e 'shift' como entradas.


def encrypt(text, shift):

    # TODO-2: Dentro da função 'encrypt', encripte o texto e retorne o resultado.

    cipher_text = ''
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        cipher_text += alphabet[new_position]
    print(f'A mensagem criptografada é: {cipher_text}')

# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Alerta de Erro: Ao tentar executar o código, você recebeu um erro de índice?
# Descubra o motivo pelo qual isso aconteceu e corrija o código.


# TODO-3: Chame a função encrypt, passando em 'text' e 'shift' como parâmetros.
encrypt(text, shift)
