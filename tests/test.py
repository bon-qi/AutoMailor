from automailor import ( Mailor, Config, Monitor )
from automailor import default_config

## using the default config
cfg_send_path, cfg_url_path = default_config("./config")
cfg_send = Config(cfg_send_path)
cfg_url = Config(cfg_url_path)

## setup actors
mailor = Mailor(**cfg_send.dict())
monitor = Monitor(**cfg_url.dict())

# if no `data/*.json` dataset setup yet.
# monitor.init_check()

# compare once
message = monitor.compare() # str
if message != None:
    status = mailor.send(message)
    print(status)
