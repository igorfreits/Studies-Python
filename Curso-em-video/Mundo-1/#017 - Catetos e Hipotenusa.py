import math
opos = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(opos, adj)
print(f'O valor da hipotenusa é {hipo:.2f}')