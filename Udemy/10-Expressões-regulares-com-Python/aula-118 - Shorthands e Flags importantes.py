"""Shorthands e Flags importantes"""
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
Jã
'''
# Busca o nome
# \w - [a-zA-Z0-9À-ú_]
# \w - [a-zA-Z0-9_] - re.A(ASCII)

# Negação
# \W - [^a-zA-Z0-9À-ú_]
# \W - [^a-zA-Z0-9_] - re.A(ASCII)

# números
# \d - [0-9]
# \D - [0-9] - Negação

# Espaços
# \s - [ \r\n\f\m\t]
# \S - [ \r\n\f\m\t] Negação

# Borda
# \b -[String vazia no começo ou final da palavra]
# \B -[String vazia no começo ou final da palavra] - Negação

# também pega letras maiúsculas - re.I
print(re.findall(r'[a-z]+', texto, flags=re.I))

# letras maiúsculas e minúsculas
print(re.findall(r'[a-zA-Z]+', texto))

# Letras maiúsculas, minusculas, números
print(re.findall(r'[a-zA-Z0-9]+', texto))

# letras maiúsculas, minusculas, números e acentos
print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))  # Gambiara

# letras maiúsculas, minusculas, números e acentos
print(re.findall(r'\w+', texto))  # Também detecta mandarim

print(re.findall(r'\w+', texto, flags=re.A))  # ASCII
print(re.findall(r'\w+', texto, flags=re.I))


print(re.findall(r'\W+', texto, flags=re.A))  # Negação/ASCII
print(re.findall(r'\W+', texto, flags=re.I))

print(re.findall(r'\d+', texto, flags=re.I))  # Números
print(re.findall(r'\D+', texto, flags=re.I))  # Negação

print(re.findall(r'\s+', texto, flags=re.I))  # Espaços
print(re.findall(r'\S+', texto, flags=re.I))  # Negação

# Bordas - Palavra iniciada e finalizada por um carácter
print(re.findall(r'\bflo\w', texto, flags=re.I))
print(re.findall(r'\w+e\b', texto, flags=re.I))
print(re.findall(r'\b\w{4}\b', texto, flags=re.I))

print(re.findall(r'flo\B', texto, flags=re.I))  # Negação

# flags
# re.A - ASCII
# re.I - IGNORECASE
# re.M - MULTILINE - ^ e $ são mais importantes
# re.S - DOTALL - Quebra de linha

cpf = '''
529.361.160-74 ABC
123.456.789-10 DEF
167.134.190-20
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf, flags=re.M))

texto2 = '''O João gosta de folia
E adora ser amado'''


print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
