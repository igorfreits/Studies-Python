"""Datetime - Trabalhando com data e hora em Python"""
from datetime import datetime, timedelta

"-https://docs.python.org/pt-br/3/library/datetime.html"


"""DATETIME: contém data e hora civis, novamente sem considerar fuso horário.
Se por exemplo o prazo de pagamento é "dia tal até 13:00",
é responsabilidade do pagador saber se estamos no horário de verão ou não."""
date = datetime(2022, 4, 21, 10, 53, 20)  # Ano-mes-dia/ hora:minutos:segundos
print(date.strftime("%d/%m/%Y %H:%M:%S"))  # Formata a data pra padrão BR
# strptime - Cria um objeto de data a partir de um string

"""TIMESTAMP: é um número que determina um momento específico.
Tipicamente é expresso como o "número de segundos desde 1/1/1970 00:00 em Londres",
mas poderia ser qualquer outra base.
A ideia do timestamp é que ele vale no mundo todo, ou seja,
ele identifica o momento exato em que algo aconteceu.
Um acontecimento com timestamp "0" aconteceu em 31/12/1969 às 21:00 no Brasil."""
date1 = datetime.strptime('20/04/2022', "%d/%m/%Y")
# Contagem de segundos dede 1/1/29170 ate a data enviada
print(date1.timestamp())

date2 = datetime.fromtimestamp(1650423600.0)  # Converte o timestamp para data
print(date2)

date3 = datetime.strptime('20/04/2015 20:00:00', '%d/%m/%Y %H:%M:%S')
# Adiciona mais tempo na data
date3 = date3 + timedelta(days=5, seconds=2*60*60)
print(date3.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/04/2015 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/2015 22:33:00', '%d/%m/%Y %H:%M:%S')

diference = d2 - d1  # Diferença de tempo
print(d1 > d2)
print(diference)
print(diference.seconds)  # Mostra em segundos(da Hora)
print(diference.total_seconds())  # Segundos totais
print(diference.days)  # Numero de dias

print(d1.time())  # Exibi so a hora
