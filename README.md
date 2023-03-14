# AutoMailor: monite and notice for academic usages

## Installation

```bash
pip install git+https://github.com/bon-qi/AutoMailor.git
```

## Usage
You can learn the usage from [examples/test.py](./examples/test.py), or see below, 

First, you need to customize your configuration into json files, luckily it has one to generate by default. 

```python
from automailor import default_config
default_config("./config") # will make configuration file: ./config/config_url.json ./config/config_send.json
```

Then, time to use this package.

```python
from automailor import ( Mailor, Config, Monitor )

# copy from a example case 
cfg_send = Config("./config/config_send.json")
cfg_url = Config("./config/config_url.json")

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

And now, information related to the webpage (usually publications) were generated in `./data/*` in form of `json` files of `html`.

The code above are integrated into one function


```python
from automailor.test import test 
if __name__ == "__main__":
    test()
```

## Hack
See the `config_xxx.json` files to hack.

The `config_send.json`,
```json
{
  // sending message
  "sender" : "[EMAIL_ADRESS]",
  "pwd" : "[SMTP_TOKEN]",
  "host_server" : "[EMAIL_SERVER]",

  //About sending message
  "receiver" : ["[RECEIVERS]"],
  "mail_title" : "[AWESOME_TITLE]",
  "content_type" : "html"
}
```

The `config_url.json`,
```json
{ 
  "save_path" : "./data",
  "requests_cfg": {
    //proxy and header, not implemented yet
    "proxies" : "127.0.0.1:7890",
    "header" : "None",
  },
  "url_dict" : { 
      "[INSTITUTE.AUTHOR]" : {
          "name"               : "[NAME_FOR_EMAIL]",
          "url"                : "[URL_TO_PUBPAGE]", 
          "xpath"              : "[XPATH_TO_EACH_PUB]", 
      },
   }
}
```

## TODO
1. Add a `streamlit` based gui for extraction of `xpath` and `url`.
2. Support more websites (e.g. twitter)

## Asking for suggestions
This project is always improving!
Issue and Pull Requests are welcomed! 


## LICENSE

Currently GPL3.

> Please do not use this SMTP email token for unconscious usages.
