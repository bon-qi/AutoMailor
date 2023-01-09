## Auto Mailor for your academic purpose
### TO BE DONE FULLY.
### Preprocessing
You need to complete `config.py` according to your email (with password for `SMTP`).
1. make a `./AutoMailor/config.py`
2. Add content below into `./AutoMailor/config.py`.
```python
sender = "[YOUR_EMAIL_NAME]@[ITS_WEBSITE]"  ## Example: example@example.com
pwd = "[PASSWORD_FOR_ITS_SMTP]"             ## Example: XAXAD12XXCD; it is according to your platform, please google for it.
host_server = "[HOST_SERVER_OF_YOUR_EMAIL]" ## Example: smtp.example.com

proxies = {                                 ## None if you do not need.
    'http' : '127.0.0.1:7890',
    'https': '127.0.0.1:7890'
}  

## TODO: Add header for anti-spider.
header = "[HEADER]" ## Header if more web settings needed
```