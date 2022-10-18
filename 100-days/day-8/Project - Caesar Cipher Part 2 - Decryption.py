alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Digite 'encode' para criptografar, digite 'decode' para descriptografar:\n")
text = input("Digite seu texto:\n").lower()
shift = int(input("Digite o deslocamento:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"O texto criptografado é: \033[34m{cipher_text}\033[m")

# TODO-1: Criar uma função chamada 'decrypt' que recebe o 'text' e 'shift' como entradas.


def decrypt(chiper_text, shift_amount):

    # TODO-2: Dentro da função 'decrypt', descriptografe o texto e retorne o resultado.
    plain_text = ""
    for letter in chiper_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"O texto descriptografado é: \033[34m{plain_text}\033[m")

    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"


# TODO-3: Chame a função decrypt, passando em 'text' e 'shift' como parâmetros.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(chiper_text=text, shift_amount=shift)
