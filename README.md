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

### Others 
1. Sending email: Please see `__main__` of `./AutoMailor/auto_mailor.py` for example.
2. Preparing for `xpath`: open your webrowser, and right push according to your sellection, `check` it in `F12` mode, and fine-tune your sellection, right click it in `F12` mode, find `copy` and `full xpath` or `xpath` you can see. (`chrome` suggested, `safari` need setting for dev-mode.)
3. For `xpath`, it can add into `./AutoMailor/url_test.py` in this mode.
```python
authors_dict = { 
    ... # other settings
    "[AUTHOR_NAME]" : {
        "name"               : "[YOUR FORMAL NAME IN EMAIL]", ## Example: Mr. Example
        "url"                : "[ITS WEBSITE]",     ## Example: example.com
        "xpath"              : "[XPATH]",           ## The Xpath you copied from web-browser, should be like '/html/body/tb[*]'
    },
```
- Tip: browser might add some `*/tbody/*` in your path, which actually not existed, so delete it if needed.