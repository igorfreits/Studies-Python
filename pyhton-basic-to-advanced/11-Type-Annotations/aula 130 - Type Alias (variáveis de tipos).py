"""Type Alias (variáveis de tipos)"""

# Type Alias (variáveis de tipos)
ListaInteiros = list[int]
DictListaInteiros = dict[str, list[int]]

um_dict_d_inteiros: DictListaInteiros = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
}
