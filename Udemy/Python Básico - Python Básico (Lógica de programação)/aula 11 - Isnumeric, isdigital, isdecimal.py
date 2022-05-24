num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

#  isnumeric, isdigit, isdecimal

print(num1.isnumeric())  # isnumeric - numeros e positivos
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():  # Retorna True se conter numeros
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não pude converter os numeros para realizar o calculo')


#  "https://docs.python.org/3/library/stdtypes.html" - documentação python
'''import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)
 
###########
#  USAGE  #
###########
 
# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True
 
# False
print(is_number('123a'))  # False'''
