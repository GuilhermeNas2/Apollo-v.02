#Classe feita para teste Unitarios e possiveis novas Features
import re
import time
from openpyxl import load_workbook
from dotenv import load_dotenv
from clienteClass import Cliente
from emailClass import Email
from excelClass import Excel
from utilsClass import Utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

        file_path = 'C:\\Users\\tkdho\\Desktop\\program\\roboLogistica\\XML\\4.xml'
        with open(file_path, "rb") as attachment:
            # Cria um objeto MIMEBase
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            
            # Codifica o conteúdo do anexo em Base64
            encoders.encode_base64(part)
            
            # Adiciona cabeçalhos ao anexo
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(file_path)}",
            )
            
            # Anexa o arquivo à mensagem
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
    if info == None or info == 'nan':
        print('ola')  
    else:
        print(info)  
  
def excelTeste():
    info = Excel.teste(3407)
    if info == None or info == 'nan':                
        print('ola')  
    else:
        print(info)  


def changePathTeste(file):       
     Utils.changePath(file)


def insertExcelTeste():
     infos = Utils.readXML('5.xml')
     listNumber = list()
     listNumber = [infos['numero']]
     info = Cliente.searchCliente(infos)    

     for i in range(0, len(listNumber),1): 
        count = 0
        while count <= 1:                     
            Excel.insertExcelN(listNumber[i], '54156/5656', info )
            count +=1

def testeFor():
     listNumber = list()
     listNumber = ['78958989']

     for i in range(0, len(listNumber),1): 
        if listNumber[i] <= 10:            
            continue
        print(listNumber[i])

def testeWord(text):
    frase= text
    textoEspeci = 'não pode ser vazio'

    result = re.search(textoEspeci, frase)
    if result:
        print('oi')
    else:
        print('nao')

def testeError():            
    driver = webdriver.Chrome() 
    driver.get(os.getenv("url"))
    time.sleep(2)        
    driver.maximize_window()
    try:    
        search = driver.find_element(By.XPATH, '//*[@id="login-container"]/form/fieldset/div[1]/div[1]/div/div/input') 
        Email.sendEmailTeste('4.xml', {'cliente':'ATACADO BF VGP'})
    except KeyError as e:
        print('search')

    except Exception as e:
        print('ola')

xmlTeste()

# emailList = Cliente.searchEmail({'cliente':"ATACADO BF VGP"})
# print(emailList)
