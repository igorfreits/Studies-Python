"""String - Template"""
from string import Template
from datetime import datetime

with open('dados_86.html', 'r') as html:
    template = Template(html.read())  # Recebe um string
    current_date = datetime.now().strftime('%d/%m/%Y')  # data atual
    # Safe_ Se nao achar o place holder ira apenas o valor
    # Se nao tiver a msm quantidade de parâmetros ira dar Error
    body_msg = template.safe_substitute(
        name='Igor Freitas', date=current_date)  # corpo

print(body_msg)
