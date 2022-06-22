"""SQLite: usando o módulo sqlite3"""

# Conexão persistente(salva os dados)
import sqlite3

connection = sqlite3.connect('database.db')  # cria a base de dados
cursor = connection.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS clients('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL'
               ')')

"""
#Insere os valores na base de dados
cursor.execute(
    'INSERT INTO clients(name, weight) VALUES("Igor Freitas", 70.3)')

Previne o SQL Injection usando uma tuple
cursor.execute(
    'INSERT INTO clients(name, weight) VALUES(?,?)', ('Michele Freitas', 50))

# Usando dicionario
cursor.execute(
    'INSERT INTO clients(name, weight) VALUES(:name,:weight)',
    {'name': 'Noah Freitas', 'weight': 25}
)

cursor.execute(
    'INSERT INTO clients VALUES(:id,:name,:weight)',
    {'id': None, 'name': 'Alice Freitas', 'weight': 60}
)
connection.commit()  # Executa a linha na base de dados"""

# # Atualiza um dado a partir do id
# cursor.execute('UPDATE clients SET name = name WHERE id =id',
#                {'name': 'Igor Freitas', 'id': 2}
#                )
# connection.commit()

# Escolhe um id para ser apagado
# cursor.execute('DELETE FROM clients WHERE id = id',
#                {'id': 2}
#                )
# connection.commit()

cursor.execute(
    'SELECT name,weight FROM clients WHERE weight >  :weight',
    {'weight': 50}
)

# Exibi as informação da tabela client
cursor.execute('SELECT * FROM clients')

# cursor.fetchall()  # Busca os valores que estão na tabela
for line in cursor.fetchall():
    identifier, name, weight = line

    print(identifier, name, weight)

cursor.close()
connection.close()
