# ANSI = ESCAPE SEQUENCE
# \033[ style; text ; back m

# \033[0;33;44m

# STYLE
# 0 = none / nada
# 1 = bold / negrito
# 4 = underline / sublinhar
# 7 = negative / inverte as configurações

#TEXT
# 30 = branco
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 35 = magenta
# 36 = ciano
# 37 = cinza

#BACKGROUND
# 40 = branco
# 41 = vermelho
# 42 = verde
# 43 = amarelo
# 44 = azul
# 45 = magenta
# 46 = ciano
# 47 = cinza

print('\033[0;30;41mOlá, Mundo!\033[m')
print('\033[4;33;44mVocê está bem?\033[m')
print('\033[1;35;43mSeja forte e corajoso\033[m')
print('\033[30;42mNão desista de seus sonhos\033[m')
print('\033[7;30mAme sua familia!\033[m')

a = 4
b = 3
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Igor'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto e branco':'\033[7;30'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, '\033[m',))

