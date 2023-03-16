from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from .utils import get_time
from .utils import font    

class Mailor(object):
    def __init__(self, sender:str, pwd:str, host_server:str, receiver:list, mail_title:str, content_type:str, **args) -> None:
        self.host_server = host_server
        self.pwd = pwd
        self.sender = sender
        self.receiver = receiver 
        self.mail_title = mail_title
        self.content_type = content_type
        pass

    ## Robustness
    def send(self, mail_content:str, **args):
        self.smtp = SMTP_SSL(self.host_server)
        self.smtp.login(self.sender, self.pwd)
        message = MIMEMultipart()
        message["Subject"] = Header(self.mail_title,'utf-8')
        message["From"] = self.sender
        message["To"] = ";".join(self.receiver)
    
        message.attach(MIMEText(mail_content,self.content_type,'utf-8'))
        self.smtp.sendmail(self.sender, self.receiver, message.as_string())  
        status = font(f"[INFO {get_time()}]", "yellow") + f"Sent: [' {mail_content} '] to {self.receiver}"
        return status


