#Classe feita para teste Unitarios e possiveis novas Features
import re
import time
from openpyxl import load_workbook
from dotenv import load_dotenv

from emailClass import Email


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


