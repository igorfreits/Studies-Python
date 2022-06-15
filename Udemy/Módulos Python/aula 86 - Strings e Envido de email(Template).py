"""String - Template"""
from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
"""A configuração de segurança lesssecureapps não está mais disponível no google"""
# Multipart - Padrão para enviar, assunto, destinatário e remetente
# Text - Corpo do email,pode ser texto ou um texto html
# image - recebe uma imagem para anexar no email
# smtplib - conecta no servidor smtp(envia o email)

# Enviando e-mails
my_email = 'your email'
my_password = 'your password'

with open('dados_86.html', 'r') as html:
    template = Template(html.read())  # Recebe um string
    current_date = datetime.now().strftime('%d/%m/%Y')  # data atual
    # Safe_ Se nao achar o place holder ira apenas o valor
    # Se nao tiver a msm quantidade de parâmetros ira dar Error
    body_msg = template.safe_substitute(
        name='Igor Freitas', date=current_date)  # corpo

msg = MIMEMultipart()
msg['from'] = 'your name'  # Remetente
msg['to'] = 'customer email'  # Destinatário
msg['subject'] = 'Atenção esse é um email de teste'  # assunto

# Se for texto simples nao precisa de parâmetros
body = MIMEText(body_msg, 'html')
msg.attach(body)  # Insere o "body" no email

with open('image.jpg', 'rb') as img:  # Anexa a imagem no email
    img.MIMEImage(img.read())
    msg.attach(img)


# Precisa abrir e fechar o smtplib
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()  # message hello
        smtp.starttls()
        smtp.login(my_email, my_password)
        smtp.send_message(msg)

        print('Email successfully sent')

    except Exception as e:
        print('email not sent...')
        print('Error:', e)
