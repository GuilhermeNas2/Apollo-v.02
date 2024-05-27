#Classe feita para teste Unitarios e possiveis novas Features

from openpyxl import load_workbook
from dotenv import load_dotenv
from clienteClass import Cliente
from emailClass import Email
from excelClass import Excel
from utilsClass import Utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



import os
import smtplib

import imaplib


load_dotenv()
def sendEmailTeste():
        
       
        email = os.getenv("email")
        password = os.getenv("passwordEmail")
        
        smtp_server = "smtp.gmail.com"
        port = 465
        sender_email = "tkdhouse2@gmail.com"
        receiver_email = email
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Verificação de Email"
        message["From"] = sender_email
        message["To"] = email

        # Crie a versão HTML da sua mensagem
        html = """\
        <html>
        <body>
            <p>Olá,<br>
            Como vai?<br>
            <a href="http://www.realpython.com">Real Python</a> 
            tem muitos ótimos tutoriais.
            </p>
        </body>
        </html>
        """
        # Adicione o HTML ao MIMEText e ao MIMEMultipart
        part = MIMEText(html, "html")
        message.attach(part)

        try:
            with smtplib.SMTP_SSL(smtp_server, port) as server:                
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
           
        except Exception as e:
            print(f"Deu errado {e}")

def emailTeste():
    imap_host = 'imap.gmail.com'
    imap_port = 993
    username = "tkdhouse2@gmail.com"
    password = os.getenv("passwordEmail")

    mail = imaplib.IMAP4_SSL(imap_host, imap_port)
    mail.login(username, password)

   
    mail.select('inbox')
    
    status, messages = mail.search(None, 'ALL')
    messages_ids = messages[0].split()
    latest_messages_ids = messages_ids[-5:]  # Pegando os últimos 5 IDs

    for msg_id in latest_messages_ids:
        status, msg_data = mail.fetch(msg_id, '(RFC822)')
        raw_email = msg_data[0][1]
        print(raw_email)  # Aqui você pode processar ou exibir o email conforme necessário

    # Fechando a conexão
    mail.logout()

def xmlTeste():    
    infos = Utils.readXML('4.xml')
    info = Cliente.searchCliente(infos)
    print(info)
  
def excelTeste():
    info = Excel.searchExcelBF(652168756198)
    print(info)


def changePathTeste(file):       
     os.rename(+file, +file )


def insertExcelTeste():
     listNumber = list()
     listNumber = [78956, 536544, 21546, 6, 2154632, 45568, 3566546, 25463214, 245214]

     for i in range(0, len(listNumber),1): 
        count = 0
        while count <= 3:                     
            Excel.insertExcelN(listNumber[i], 'teste:'+str(i), "R$54" )
            count +=1

def testeFor():
     listNumber = list()
     listNumber = [78956, 536544, 21546, 10, 2154632, 45568, 3566546, 25463214, 245214]

     for i in range(0, len(listNumber),1): 
        if listNumber[i] <= 10:            
            continue
        print(listNumber[i])
        
xmlTeste()


