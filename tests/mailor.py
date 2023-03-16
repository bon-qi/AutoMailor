import time
from automailor import (Config, Mailor)

if __name__ == "__main__":
    config = Config()
    automail_qi = Mailor(config.sender, config.pwd, config.host_server)
    for i in range(300):
        automail_qi.send_to(
            receiver=["2308224300@qq.com"],
            mail_content="<h1>Hola World!</h1>",
            mail_title="你好呀"
        )
        time.sleep(2)
