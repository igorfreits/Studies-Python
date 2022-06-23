"""CRUD com Pymysql no MySQL e Mariadb Server"""

import pymysql.cursors
from contextlib import contextmanager
# Xampp(Cria um servidor) e MySQL Workbench
# Acessa o banco de dados do servidor
# CRUD - CREATE, READ, UPDATE, DELETE


@contextmanager
def connect():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    # FECHA A CONEXÃO
    try:
        yield connection
    finally:
        print('connection is close')
        connection.close()

# INSERE UM REGISTRO NA BASE DE DADOS#
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome,idade,peso) VALUES'\
#             '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Igor', 'Freitas', 23, 70))
#         connection.commit()


# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'

#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55),
#         ]
#         cursor.executemany(sql, dados)
#         connection.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         connection.commit()

# DELETA QUANTIDADE DETERMINADA DE REGISTROS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN  (%s, %s, %s)'
#         cursor.execute(sql, (6, 7, 8))
#         connection.commit()

# DELETA REGISTRA ENTRE UM RANGE
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10,12))
#         connection.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
with connect() as connection:
    with connection.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id = %s'
        cursor.execute(sql, ('JOÃO', 5))
        connection.commit()

# FECHA O CURSOR
with connect() as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        result = cursor.fetchall()

        for line in result:
            print(line)
