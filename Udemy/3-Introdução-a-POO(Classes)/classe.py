# aula 73
class MyClass:
    """Regular document

    Conforme qualquer outra documentação que voce tenha usado anteriormente
    """
    atribute1 = 1
    atribute2 = 'Value'

    def __init__(self, text):
        """Inicializa os dados

        :parameter texto: O texto da classe
        :type text = str
        """
        self.texto = text
        self.display_text(text)

    @staticmethod
    def display_text(text):
        """Método que exibe um texto de 100 caracteres na tela
        :parameter text: Um texto de 100 caracteres
        :type text = str

        :return: O texto de 100 caracteres
        :return type = str

        :raise ValueError: Se o texto tiver mais de 100 caracteres
        :raises  TypeError: Se o texto não for uma str
        """

        if not isinstance(text, str):
            raise TypeError("O texto precisar ser uma String")
        if len(text) > 100:
            raise ValueError('O texto precisar ter 100 caracteres ou menos')
        return text
