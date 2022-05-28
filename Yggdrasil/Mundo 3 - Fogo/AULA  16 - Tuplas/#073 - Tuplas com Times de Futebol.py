times = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo',
         'Corinthians', 'Internacional', 'Cruzeiro', 'São Paulo',
         'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba',
         'Bahia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa',
         'Atlético Paranaense', 'Vitória')

# print(f'Lista de times do Brasileirão: {times}')

print('=-'*60)

print(f'Os 5 primeiros são: {times[:6]}')

print('=-'*40)

print(f'Os 4 últimos são: {times[::-5]}')

print('=-'*40)

print(f'Times em ordem alfabética: {sorted(times)}')

print('=-'*40)

print(f'O São Paulo esta na {times.index("São Paulo")+1}ª posição')
