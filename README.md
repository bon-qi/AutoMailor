## The package allow you to monite and send email to any research webpage

> Follow the usage below to use it 

### Installation

```bash
pip install git+https://github.com/bon-qi/automailor.git
```

### Usage

Basically, you can follow how to use from [examples/test.py](./examples/test.py), the main loop of this software is below.

0. Import packages and modules 

```python
from automailor import ( Mailor, Config, Monitor )
from automailor import default_config
```

1. set up configs of `Mailor` and `Monitor`, I have made a default setting to you.

```python
default_config("./config")
cfg_send = Config("./config/config_send.json")
cfg_url = Config("./config/config_url.json")
```

2. define our `mailor` and `monitor` from config.

```python
mailor = Mailor(**cfg_send.dict())
monitor = Monitor(**cfg_url.dict())
```

3. Begin the mainloop!
```python
monitor.init_check()
while True:
    message = monitor.compare() # str
    if message != None:
        mailor.send(message)
    time.sleep(2)

```

## TODO
1. Add a `streamlit` based gui for extraction of `xpath` and `url`.
2. Support more websites (e.g. twitter)
