# import time
# from auto_mailor import AutoMailor

# from tqdm import trange, tqdm
# import config
import requests
from lxml import etree
import json

from url_test import authors_dict
from utils import fg
from authors.jon_barron import *



def main():
    response = requests.get(url)
    html = response.content
    et = etree.HTML(html)
    coarse_unites = []
    for i, coarse_unit in enumerate(et.xpath(xpath)):
        coarse_html = etree.tostring(coarse_unit)
        coarse_unites.append({i:str(coarse_html)})
        pass
    # print(coarse_unites)



    t = json.dumps(coarse_unites, separators=(",",":"), indent=4)
    with open(f"./data/{name}.json","w") as file:
        file.write(t)
    pass
# def main():
#     for name, info in zip(authors_dict.keys(), authors_dict.values()):
#         print(fg.orange,"Getting ", info["url"],fg.orange)
#         try:
#             response = requests.get(info["url"])
#             web_old = response.text

#             with open(f"./beta/{name}.html",'r') as file:
#                 web_new = file.read()
            
#             if web_new == web_old:
#                 print(f"{fg.blue}{name} has no updates{fg.blue}")

#             else :
#                 ## analysis first
#                 et = etree.HTML(web_new)

#                 print(len(info["paper_title"](et)))
#                 print(len(info["paper_authors"](et)))
#                 print(len(info["paper_conference"](et)))

#                 for title, authors,conference in zip(
#                     info["paper_title"](et),
#                     info["paper_authors"](et),
#                     info["paper_conference"](et),
#                 ):
#                     # print("Title: ", title)
#                     # print("Authors: ", authors)
#                     # print("Conference: ", conference)
#                     # print("*"*140)
#                     pass

#                 ## if it was update
#                 ## Email here
#                 print(f"{fg.lightred}{name} has updates!{fg.lightred}")
#                 with open(f"./beta/{name}_new.html",'w') as file:
#                     file.write(web_new)
#             print(fg.lightblue,"Done!",fg.lightblue)
#         except:
#             print(fg.cyan,"Get ", info["url"], "Failed!",fg.cyan)

if __name__ == "__main__":
    main()
