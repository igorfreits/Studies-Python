alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine os encrypt() e decrypt() em uma função chamada caesar().


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        elif cipher_direction == "decode":
            new_position = position - shift_amount
            end_text += alphabet[new_position]
    print(f"O texto {cipher_direction} é: \033[34m{end_text}\033[m")

# TODO-2: Chame a função caesar() em vez de encrypt() e decrypt().


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
