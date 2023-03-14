# The package allow you to monite and send email to any research webpage

> Follow the usage below to use it 

## Installation

```bash
pip install git+https://github.com/bon-qi/automailor.git
```

## Usage
You can learn the usage from [examples/test.py](./examples/test.py), or see below, 

```python
from automailor import ( Mailor, Config, Monitor )
from automailor import default_config

# copy from a example case 
cfg_send_path, cfg_url_path = default_config("./config")
cfg_send = Config(cfg_send_path)
cfg_url = Config(cfg_url_path)

# define our `mailor` and `monitor` from config.
mailor = Mailor(**cfg_send.dict())
monitor = Monitor(**cfg_url.dict())

# begin the loop to monitor
monitor.init_check()
while True:
    message = monitor.compare() # str
    if message != None:
        mailor.send(message)
    time.sleep(200)
```

## Hack
After any run, the `config_xxx.json` file which define the procedure of spiding, you can editting it.

> Please do not use this SMTP email token for bad usages...

## TODO
1. Add a `streamlit` based gui for extraction of `xpath` and `url`.
2. Support more websites (e.g. twitter)
