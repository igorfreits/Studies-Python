"""
JSON - JavaScript Object Notation
è um formato de troca de dados entres sistemas e programas muito leve e de fácil utilização.
Muito utilizado em APIs
"""

import json

from matplotlib.font_manager import json_load
from dados_83 import *
"https://docs.python.org/pt-br/3/library/json.html"

"""
DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number(int)	    int
number(real)	float
true	        True
false	        False
null	        None

"""
list = [1, 2, 3, 4, 5, 6, 7]
dados_json = json.dumps(list)  # convert para  json
print(dados_json)
print(type(dados_json))  # <class 'str'> - array

dados_json2 = json.dumps(clients_dictionary, indent=4)  # indentation
print(dados_json2)
print(type(dados_json2))  # <class 'str'> - object

print(clients_json)
dictionary = json.loads(clients_json)  # convert para Python
print(type(dictionary))  # <class 'dict'>

for key, value in dictionary.items():
    print(key)
    print(value)

with open('clientes_json', 'r') as file:  # cria um arquivo de escrita json
    json.dump(clients_dictionary, file, indent=4)

with open('clientes_json', 'r') as file:  # convert o arquivo json criado
    dados = json.load(file)
print(dados)
