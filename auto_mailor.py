from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from utils import get_time
from utils import fg    

class AutoMailor(object):
    def __init__(self, sender:str, pwd:str, host_server:str) -> None:
        self.host_server = host_server
        self.pwd = pwd
        self.sender = sender
        pass

    def send_to(self, receiver: list = ['2308224300@qq.com'],
                mail_content: str = '自动发送的消息 勿回',
                mail_title: str = "[自动发送 de Qi]"):
        self.smtp = SMTP_SSL(self.host_server)
        self.smtp.login(self.sender, self.pwd)
        message = MIMEMultipart()
        message["Subject"] = Header(mail_title,'utf-8')
        message["From"] = self.sender
        message["To"] = ";".join(receiver)
    
        message.attach(MIMEText(mail_content,'plain','utf-8'))
        self.smtp.sendmail(self.sender, receiver, message.as_string())  
        self.quit()      
        print(f"{fg.yellow}[INFO {get_time()}]{fg.lightgrey} Sent: [",
              mail_content, "] to ", receiver)
    def quit(self):
        self.smtp.quit()

if __name__ == "__main__":
    import config
    import time
    automail_qi = AutoMailor(config.sender, config.pwd, config.host_server)
    for i in range(300):
        automail_qi.send_to(
            # ["1287974345@qq.com", "2834637388@qq.com", "961850163@qq.com", "2308224300@qq.com"],
            receiver=["songbr@mail.ustc.edu.cn"],
            mail_content="[自动发送，请勿回复]你好呀",
            mail_title="你好呀"
        )
        time.sleep(2)
