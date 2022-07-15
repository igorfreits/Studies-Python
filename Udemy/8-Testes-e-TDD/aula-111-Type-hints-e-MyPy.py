"""Type hints e MyPy

-https://docs.python.org/pt-br/3/library/typing.html

-No VsCode precisar colocar nas configurações
-No pycharm precisa instalar a biblioteca MyPy e ativar o plugin pro terminal
"""
from typing import List, Union, Tuple, Dict

# -Primitivos
numero: int = 10
flutuante: float = 10.5
booleans: bool = False
string: str = 'texto'

# -Sequências
# Verifica se é uma lista de inteiros
lista: List[int] = [1, 2, 3]

# Verifica se é uma lista de inteiros ou strings
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'texto']

# Precisa passar especificamente cada item
tuplas: Tuple[int, int, int, str] = (1, 2, 3, 'texto')

# -Dicionários e conjuntos
# Verifica se é um dicionário com chave string com valores string ou int
pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Igor', 'sobrenome': 'Freitas', 'idade': 23}
