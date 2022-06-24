"""Sobrecarga de operadores(POO)"""

"""No Python,  o comportamento dos operadores é definido por métodos especiais.
-Vamos alterar o comportamento de operadores com
classes definidas pelo usuário"""

"""
# Métodos Mágicos
Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""


class Rectangle:  # Retângulo
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f'<class Rectangle({self.x, self.y})>'

    """__repr()__ serve para representar um objeto como uma string.
    Não precisa ser chamado diretamente. Toda vez que o Python precisa
    resolver um objeto como string, __repr__() será chamado automaticamente.
    Vários tipos de objetos implementam __repr__() por padrão. Para objetos,
    normalmente __repr__() devolve a descrição e a referência em
    memória para o objeto.
    A grande vantagem de __repr__() é justamente poder reescrevê-lo,
    como fiz aqui.
    Ao invés de escrever o objeto como <tipo + referência>"""

    def __add__(self, other):  # Soma +
        # Recebe um obj e o outro obj
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Rectangle(new_x, new_y)

    def __gt__(self, other):  # Menor
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 > a2:
            return True
        else:
            return False

    def __lt__(self, other):  # Maior >
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 < a2:
            return True
        else:
            return False

    def __et__(self, other):  # Igualdade
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = r1 + r2
print(r3 == r1)
