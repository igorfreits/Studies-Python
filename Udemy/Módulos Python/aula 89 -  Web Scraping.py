""" Web Scraping"""
# Navegar pelo site e baixar os dados
import requests
from bs4 import BeautifulSoup

# requests - requisição(BAicar html)
# bs4 - manipulação do html

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for question in html.select('.s-post-summary.js-post-summary'):
    title = question.select_one('.s-link')
    data = question.select_one('.relativetime')
    votes = question.select_one('.s-post-summary--stats-item-number')
    print(data.text, title.text, votes.text, sep='\t')
