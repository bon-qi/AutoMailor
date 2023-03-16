import os
import requests
from lxml import etree
import datetime
import time
import arxivscraper

from .dataset import Dataset 
from .utils import font , get_time, unique

class Monitor(object):
    def __init__(self, url_dict:dict, save_path:str, requests_cfg:dict, arxiv_cfg:dict, **args):
        self.save_path = save_path
        if not os.path.exists(save_path): os.mkdir(save_path)
        self.url_dict = url_dict
        self.requests_cfg = requests_cfg
        self.arxiv_cfg = arxiv_cfg
        pass

    ## note: arxiv need proxy inside china.
    def _arxiv(self):
        today = str(datetime.date.today())
        categories = self.arxiv_cfg['categories']
        info = list() 
        for key, value in categories.items():
            scraper = arxivscraper.Scraper(category=key, date_from=today, date_until=today, filters={ 'categories' : value })
            info_tmp = scraper.scrape()
            info.extend(info_tmp)
            time.sleep(10)

        ret = f"<h2> <span style=\"color:#6A00B8\"> Arxiv of {today} : ({len(info)}) updates </span> </h2>" 
        for item in info:
            ## item: dict ('title', 'id', 'abstract', 'categories', 'created', 'updated', 'authors':list. 'affiliation':list, 'url')
            ret += f"""
                    <br> <b>{item['title']}</b>
                    <br/> {", ".join(item["authors"])} 
                    <br/> {", ".join(unique(item["affiliation"]))}
                    <br/> Created ({item['created']}), updated ({item['updated']}). 
                    <!-- <br/> {item['abstract']} -->
                    <br/> <a href={item['url']}>arxiv</a> 
                    <br/>
                    """
        return ret


    def _twitter(self):
        pass

    def init_check(self):
        for name, info in zip(self.url_dict.keys(),self.url_dict.values()):
            # get content and search from it.
            try: ## robustness
                response = requests.get(info["url"])
            except:
                print(font(f"[INFO {get_time()}] ","red"), f"Got {info['url']} failed.")
                continue
            et = etree.HTML(response.content)
            pubs_node = et.xpath(info["xpath"]) 

            # get them together
            pubs = dict()
            n = len(pubs_node)
            for i, pub_node in enumerate(pubs_node):
                pub_html = etree.tostring(pub_node)
                pubs.update({f"{n-i}" : str(pub_html,'utf-8')})

            # init Dataset 
            dataset =  Dataset(f"{self.save_path}/{name}.json")
            print(font(f"[INFO {get_time()}]", "lightblue"), f"{name} ({info['url']}) init with {len(pubs)} pub(s).")
            dataset.write(pubs)
        print("")
        pass

    def _check(self):
        ret = dict()
        for name, info in zip(self.url_dict.keys(), self.url_dict.values()):
            # get content and search from it.
            try: ## robustness
                response = requests.get(info["url"] )
            except:
                print(font(f"[INFO {get_time()}] ","red"), f"Got {info['url']} failed.")
                continue

            et = etree.HTML(response.content)
            pubs_node = et.xpath(info["xpath"]) 

            # get them together
            pubs_new = dict()
            n = len(pubs_node)
            for i, pub_node in enumerate(pubs_node):
                pub_html = etree.tostring(pub_node)
                pubs_new.update({f"{n-i}" : str(pub_html,'utf-8')})

            # get old Dataset 
            dataset =  Dataset(f"{self.save_path}/{name}.json")
            pubs_old = dataset.read()
            if pubs_old != pubs_new:
                # view as difference of sets
                pub_new = list(set(pubs_new.values()).difference(set(pubs_old.values())))
                # pub_new = extra_keys(keys_new, pubs_new)
                ret.update({name:pub_new})
                print(font(f"[INFO {get_time()}]","lightgreen"),f"{name} ({info['url']}) has {len(pub_new)} new pub(s).")
                dataset.write(pubs_new)
            else:
                print(font(f"[INFO {get_time()}]","lightblue"), f"{name} ({info['url']}) has no new pub.")
        return ret
        ##  ret = {
        ##       "name" : [ "new_pub1" , "new_pub2" ],
        ##  }


    def compare(self):
        message = str() + self._arxiv()
        new_pubs = self._check()
        ## check for new pub
        if new_pubs != dict() and new_pubs != None:
            for name, pubs in zip(new_pubs.keys(), new_pubs.values()):
                message += f"<h2> <span style=\"color:#6A00B8\"> {self.url_dict[name]['name']} </span>  <h2>  has {len(pubs)} pubs,  </br> </br>"
                for pub in pubs:
                    message += pub
                    message += "</br></br>"
            return message

        else:
            print(font(f"[INFO {get_time()}]", "yellow"), "no any new pub.")
        print("")
        return  message

