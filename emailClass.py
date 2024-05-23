import os
import smtplib
import imaplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class Email:
    load_dotenv()
    def sendEmailTeste(receive):       
        
            email = os.getenv("email")
            password = os.getenv("passwordEmail")
            print(1)
            smtp_server = "smtp.gmail.com"
            port = 465
            sender_email = email
            receiver_email = receive
            
            message = MIMEMultipart("alternative")
            message["Subject"] = "Verificação de Email"
            message["From"] = sender_email
            message["To"] = email
            print(2)
            
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

            part = MIMEText(html, "html")
            message.attach(part)

            try:
                with smtplib.SMTP_SSL(smtp_server, port) as server:                
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
            
            except Exception as e:
                print(f"Deu errado {e}")