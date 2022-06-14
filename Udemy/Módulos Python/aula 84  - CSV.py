"""CSV - Comma Separated Values

(Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv
with open('clients.csv', 'r') as file:
    datas1 = csv.reader(file)  # dados

    # Mostra valores em um dict - Dicionário ordenado
    datas2 = [x for x in csv.DictReader(file)]

    # for data1 in datas1:
    #     print(data1)

    # for data2 in datas2:
    #     print(data2)
    #     print()
    #     # as chaves sao os nomes da coluna
    #     print(data2['Name'], data2['last_name'])

# for data2 in datas2:
#     print(data2)

with open('clients2.csv', 'w') as file:
    write = csv.writer(
        file,
        delimiter=',',  # Delimitador (separa com ',')
        # Coloca aspas " "(recomendado usar caso arquivo tenhas aspas)
        quotechar='"',
        quoting=csv.QUOTE_ALL  # Sera todo delimitado todo em aspas ARROZ
    )
    keys = datas2[0].keys()
    keys = list(keys)
    write.writerow(
            [
                keys[0],
                keys[1],
                keys[2],
                keys[3]
            ]
        )
    for data2 in datas2:
        write.writerow(
            [
                data2['Name'],
                data2['last_name'],
                data2['E-mail'],
                data2['Phone']
            ]
        )





    
