import os
import time
import requests
from lxml import etree

from utils import fg, extra_keys, get_time
from dataset import DatasetJS
from auto_mailor import AutoMailor
import config
from url_test import authors_dict


def check(author_dict, proxies=None,header=None):
    ret = dict()
    for name, info in zip(author_dict.keys(),author_dict.values()):
        # get content and search from it.
        try: ## robustness
            response = requests.get(info["url"], proxies=proxies)
        except:
            print(f"{fg.red}[INFO {get_time()}]{fg.lightgrey} Got {info['url']} failed.")
            continue

        et = etree.HTML(response.content)
        pubs_node = et.xpath(info["xpath"]) 
        
        print(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} Got {info['url']}.")
        
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
            pub_new = list(set(unites_new.values()).difference(set(unites_old.values())))
            # pub_new = extra_keys(keys_new, unites_new)
            ret.update({name:pub_new})
            print(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has {len(pub_new)} new pub(s).")
            dataset.write(unites_new)
        else:
            print(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has no new pub.")
    return ret
##  ret = {
##       "name" : [ "new_pub1" , "new_pub2" ],
##  }

def test(authors_dict):
    ret = dict()
    for name, info in zip(authors_dict.keys(),authors_dict.values()):
        # get DatasetJS
        new = DatasetJS(f"./data/{name}.json")
        old = DatasetJS(f"./data_test/{name}.json")
        new = new.read()
        old = old.read()
        if new != old:
            pub_new = list(set(new.values()).difference(set(old.values())))
            # pub_new = extra_keys(keys_new, new)
            ret.update({name:pub_new})
            print(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has {len(pub_new)} new pub(s).")
        else:
            print(f"{fg.lightblue}[INFO {get_time()}]{fg.lightgrey} {name} has no new pub.")
    return ret


if __name__ == "__main__":
    if not os.path.exists("./data/"): os.mkdir("./data/")

    automailor = AutoMailor(config.sender, config.pwd, config.host_server)
    while True:
        new_pubs = check(authors_dict, config.proxies, config.header)
        ## check for new pub
        if new_pubs != dict() and new_pubs != None:
            message = str()
            for name, pubs in zip(new_pubs.keys(), new_pubs.values()):
                message += f"<b> <span style=\"color:#a51e37\"> {authors_dict[name]['name']} </span>  <b>  has {len(pubs)} pubs,  </br> </br>"
                for pub in pubs:
                    message += pub
                    message += "</br>"
            automailor.send_to( receiver=config.receiver, mail_content=message, 
                                content_type='html', mail_title=config.title)            

        print(f"{fg.lightgreen}[INFO {get_time()}]{fg.lightgrey} end of one iter")
        print()
        time.sleep(10)
