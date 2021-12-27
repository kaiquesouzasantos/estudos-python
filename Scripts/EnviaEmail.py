import os
import smtplib
from email.message import EmailMessage

try:
    EMAIL_REMETENTE = str(input('Email do Remetente: '))
    EMAIL_SENHA = str(input('Senha: '))

    EMAIL_TITULO = str(input('Titulo do Email: '))
    EMAIL_DESTINATARIO = str(input('Destinatário: '))
    EMAIL_MENSAGEM = str(input('Mensagem: '))

    msg = EmailMessage()
    msg['Subject'] = EMAIL_TITULO # Subject => TITULO
    msg['FROM'] = EMAIL_REMETENTE # FROM => REMETENTE
    msg['To'] = EMAIL_DESTINATARIO # To => DESTINATARIO
    msg.set_content(EMAIL_MENSAGEM)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_REMETENTE, EMAIL_SENHA)
        smtp.send_message(msg)
    
    print('EMAIL ENVIADO COM SUCESSO!\nPrograma Finalizado...')

except:
    print('FALHA NO ENVIO DO EMAIL!\nPrograma Finalizado...')