"""Type Union (mais de um tipo)"""

string_e_inteiros: str | int = 1  # Union

string_e_inteiros: str | int = 'a'  # Sem erros
string_e_inteiros: str | int = 2  # Sem erros

lista: list[int | str] = [1, 2, 3, 'a', 'b', 'c']
