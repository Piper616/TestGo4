from django.test import TestCase
import smtplib
from email.mime.text import MIMEText
from django.conf import settings

def send_email():
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login('testgo.proyecto@gmail.com','testgo619.')

        # Construimos el mensaje simple
        mensaje = MIMEText("""Este es el mensaje de las narices""")
        mensaje['From']= 'testgo.proyecto@gmail.com'
        mensaje['To']="f.diazmendez@gmail.com"
        mensaje['Subject']="Tienes un correo"

        # Envio del mensaje
        mailServer.sendmail('testgo.proyecto@gmail.com',"f.diazmendez@gmail.com", mensaje.as_string())
    except Exception as e:
        print(e)

# Create your tests here.
