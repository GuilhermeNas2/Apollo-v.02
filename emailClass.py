import os
import smtplib
import imaplib

from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from clienteClass import Cliente

class Email:
    load_dotenv()
   
    def sendEmailTeste(archive, cliente):               
            email = os.getenv("email")
            password = os.getenv("passwordEmail")
            emailList = Cliente.searchEmail(cliente)

            smtp_server = "smtp.gmail.com"
            port = 465
            sender_email = email
            
            for i in range(0, len(emailList),1):
                receiver_email = 'tkdhouse2@gmail.com'
                message = MIMEMultipart("alternative")
                message["Subject"] = "Verificação de Email"
                message["From"] = sender_email
                message["To"] = email            
                
                html = """\
                <html>
                <body>
                    <p>Olá,<br>
                    Como vai?<br>
                    Segue Xml's com falta de informações, favor verificar.
                    </p>
                </body>
                </html>
                """

                part = MIMEText(html, "html")
                message.attach(part)

                file_path = os.getenv('pathXML')+archive
                with open(file_path, "rb") as attachment:
                    
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())                   
                    
                    encoders.encode_base64(part)                    
                    
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {os.path.basename(file_path)}",
                    )                   
                   
                    message.attach(part)

                try:
                    with smtplib.SMTP_SSL(smtp_server, port) as server:                
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message.as_string())
                
                except Exception as e:
                    print(f"Deu errado {e}")

