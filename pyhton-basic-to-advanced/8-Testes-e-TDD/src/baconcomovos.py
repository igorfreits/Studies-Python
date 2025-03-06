"""aula-112-Unittest#2

1-Receber um numero inteiro
2-Saber se o número é multiplico de 3 e 5
    Bacon com ovos
3 - Saber o numero NÂO é múltiplo de 3 e 5
    Passar fome
4 - Saber se o numero é múltiplo somente de 5
    Ovos
5 - Passar fomeSaber se um numero é múltiplo somente de 3
    Bacon
"""


def bacon_com_ovos(numero):
    assert isinstance(numero, int), 'numero dever ser int'
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Bacon com ovos'
    if numero % 3 == 0:
        return 'Bacon'
    if numero % 5 == 0:
        return 'Ovos'
    return 'Passar fome'
