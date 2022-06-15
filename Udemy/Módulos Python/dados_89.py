import requests
from bs4 import BeautifulSoup

# requests - requisição(BAicar html)
# bs4 - manipulação do html


url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for questions in html.select('.s-post-summary.js-post-summary'):
    title = questions.select_one('.s-link')
    date = questions.select_one('.relativetime')
    votes = questions.select_one('.s-post-summary--stats-item-number.mr4')
    
    print(date.text, title.text, votes.text)
