import psycopg2

conexão = psycopg2.connect(
    dbname="credito_analise",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432")

cursor = conexão.cursor()
