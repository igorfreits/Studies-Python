from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: Crie condições para manter os números, símbolos e espaços como eles estão.
        # Você pode corrigir o código para manter o número/símbolo/espaço quando o texto é codificado/decodificado?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"O texto {cipher_direction} é: \033[34m{end_text}\033[m")


# TODO-1: Importe e use o módulo art.py, que contém o logotipo do programa.
print(logo)


should_continue = True
while should_continue:
    direction = input(
        'Digite "encode" para criptografar, digite "decode" para descriptografar:\n').lower()
    text = input("Digite sua mensagem\n").lower()
    shift = int(input("Digite o número de deslocamento:\n"))

    # TODO-2: E se o usuário inserir um deslocamento maior que o número de letras do alfabeto?
    # Tente executar o programa e inserir um número de turno de 45.
    # Adicione algum código para que o programa continue funcionando mesmo que o usuário insira um número de turno maior que 26.
    # Dica: Pense em como você pode usar o módulo (%).
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # TODO-4: Você pode descobrir uma maneira de perguntar ao usuário se ele deseja reiniciar o programa de cifra?
    # por exemplo. Digite 'sim' se quiser ir novamente. Caso contrário, digite 'não'.
    # Se eles digitarem 'yes', peça-lhes a direção/texto/deslocamento novamente e chame a função caesar() novamente?
    # Dica: Tente criar um loop while que continue a executar o programa se o usuário digitar 'sim'.

    result = input(
        "Digite 'sim' se quiser ir novamente. Caso contrário, digite 'não'.\n").lower()
    if result == "n":
        should_continue = False
        print("Goodbye")
