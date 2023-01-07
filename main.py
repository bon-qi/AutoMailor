import time
# from tqdm import trange, tqdm
import requests
from lxml import etree
import json

from utils import fg, extra_keys, get_time
from dataset import DatasetJS
from auto_mailor import AutoMailor
import config

def check(author_dict, log):
    ret = []
    for name, info in zip(authors_dict.keys(),authors_dict.values()):
        # get content and search from it.
        ## robustness
        response = requests.get(info["url"])
        et = etree.HTML(response.content)
        pubs_node = et.xpath(info["xpath"]) 
        
        # get them together
        unites_new = dict()
        n = len(pubs_node)
        for i, unit in enumerate(pubs_node):
            unit_html = etree.tostring(unit)
            unites_new.update({f"{n-i}" : str(unit_html,'utf-8')})

        # get DatasetJS
        dataset = DatasetJS(f"./data/{name}.json")
        unites_old = dataset.read()
        if unites_old != unites_new:
            keys_new = list(set(unites_new.keys()).difference(set(unites_old.keys())))
            pub_new = extra_keys(keys_new, unites_new)
            ret.append({name:pub_new})
            log.append(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has {len(pub_new)} new pub(s).")
            dataset.write(unites_new)
        else:
            log.append(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has no new pub.")
    return ret
##  ret = [ 
##      { "name" : [ "new_pub1" , "new_pub2" ] }
##  ]

def test(authors_dict, log):
    ret = []
    for name, info in zip(authors_dict.keys(),authors_dict.values()):
        
        # get DatasetJS
        new = DatasetJS(f"./data/{name}.json")
        old = DatasetJS(f"./data_test/{name}.json")
        new = new.read()
        old = old.read()
        if new != old:
            keys_new = list(set(new.keys()).difference(set(old.keys())))
            pub_new = extra_keys(keys_new, new)
            ret.append({name:pub_new})
            log.append(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has {len(pub_new)} new pub(s).")
        else:
            log.append(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has no new pub.")
    return ret


if __name__ == "__main__":
    from url_test import authors_dict
    automailor = AutoMailor(config.sender, config.pwd, config.host_server)

    while True:
        time.sleep(5)
        log = []
        new_pubs = check(authors_dict, log)

        ## check for new pub
        if new_pubs != list():
            message = str()
            for i, new_pub in enumerate(new_pubs):
                name = list(new_pub.keys())[0]
                pubs = list(new_pub.values())[0]
                message += f" <b>{authors_dict[name]['name']}<b>  has {len(pubs)} pubs,  </br> </br>"
                for pub in pubs:
                    message += pub
                    message += "</br>"
            automailor.send_to( receiver=["2308224300@qq.com"], mail_content=message, 
                                content_type='html', mail_title="[自动放送] 新情报")            
            
        for info in log:
            print(info)
        print(f"{fg.lightgreen}[INFO {get_time()}]{fg.lightgrey} end of one iter")
