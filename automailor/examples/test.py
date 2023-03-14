from automailor import ( Mailor, Config, Monitor )
from automailor import default_config

default_config("./config")

cfg_send = Config("./config/config_send.json")
cfg_url = Config("./config/config_url.json")

mailor = Mailor(**cfg_send.dict())
monitor = Monitor(**cfg_url.dict())

monitor.init_check()
while True:
    message = monitor.compare() # str
    if message != None:
        mailor.send(message)
    time.sleep(2)
