""" Web Scraping"""
# Navegar pelo site e baixar os dados
import requests
from bs4 import BeautifulSoup

"""Beautiful Soup é uma biblioteca Python de extração de dados de arquivos HTML e XML.
Ela funciona com o seu interpretador (parser) favorito a fim de prover maneiras
mais intuitivas de navegar, buscar e modificar uma árvore de análise (parse tree).
Ela geralmente economiza horas ou dias de trabalho de programadores ao redor do mundo.

-https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
"""


"""Permite que você envie solicitações HTTP em Python.
Uma vez que o uso de uma API implica em enviar solicitações HTTP e receber respostas,
a biblioteca Requests permite que você utilize APIs no Python.Vamos demonstrar o uso de uma API
de tradução de idioma aqui para você veja um um exemplo de como ela funciona.

-https://requests.readthedocs.io/projects/pt/pt_BR/latest/user/quickstart.html"""

# requests - requisição(BAiXar html)
# bs4 - manipulação do html

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for question in html.select('.s-post-summary.js-post-summary'):
    title = question.select_one('.s-link')
    data = question.select_one('.relativetime')
    votes = question.select_one('.s-post-summary--stats-item-number')
    print(data.text, title.text, votes.text, sep='\t')
