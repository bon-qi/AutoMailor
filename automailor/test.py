import time

from .mailor import Mailor
from .monitor import Monitor 
from .config import Config

def test():
    cfg_send = Config("./examples/config_send.json")
    cfg_url = Config("./examples/config_url.json")

    mailor = Mailor(**cfg_send.dict())
    monitor = Monitor(**cfg_url.dict())

    monitor.init_check()
    while True:
        message = monitor.compare() # str
        if message != None and message != str():
            mailor.send(message)
        time.sleep(2)
