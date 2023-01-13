import os

sender = "automail_qi@163.com"
pwd = os.environ['SMTP_PWD']
host_server = "smtp.163.com"

proxies = {
    'http' : '127.0.0.1:7890',
    'https': '127.0.0.1:7890'
}

## TODO: Add header for anti-spider.
header = {
   "" : ""
}