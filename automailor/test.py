import time

from .mailor import Mailor
from .monitor import Monitor 
from .config import Config
from .utils import default_config

def test():
    cfg_send_path, cfg_url_path = default_config("./config")
    cfg_send = Config(cfg_send_path)
    cfg_url = Config(cfg_url_path)

    mailor = Mailor(**cfg_send.dict())
    monitor = Monitor(**cfg_url.dict())

    monitor.init_check()
    while True:
        message = monitor.compare() # str
        if message != None and message != str():
            mailor.send(message)
        time.sleep(2)
