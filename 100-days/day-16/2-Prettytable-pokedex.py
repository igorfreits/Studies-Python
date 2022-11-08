from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu',
                 'Squirtle', 'Charmander', 'Bulbasaur', 'Eevee', 'Gengar', 'Lucario'])
table.add_column('Type', ['Electric', 'Water', 'Fire',
                 'Grass', 'Normal', 'Ghost', 'Fighting'])

table.align = 'l'  # alinha a tabela à esquerda
print(table)
