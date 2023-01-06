from lxml import etree
class LabPublications(object):
    def __init__(self,name:str ,url:str,content_extration:dict) -> None:
        
        pass

authors_dict = { 
## Germany && Switherland && British 
    ### Germany
    "mpi.andreas_geiger" : {
        "url"                   :"https://www.cvlibs.net/publications.php", 
        "pub_unit"              : '/html/body/div[2]/div[@class="publication_container"]/', ## and '/html/body/div[2]/div[@class=publication_detail]'
        # "paper_title"           :lambda etree: etree.xpath('.//div[@class="publication_title"]/b/text()'),
        # "paper_conference"      :lambda etree: etree.xpath('.//div[@class="publication_title"]/text()')[1::2],
        # "paper_authors"         :lambda etree: etree.xpath('.//div[@class="publication_title"]/text()')[::2]
    }          ## Andreas Geiger
    ,
    "google.jon_barron" : {
        "url"                   :"https://jonbarron.info",
        "pub_unit"              :"/html/body/table/tbody/tr/td/table[3]/tbody/tr/",
        "unit2title"            :"",
        "unit2conference"       :"",
        "unit2authors"          :"",
        # "unit2content"          : lambda unit: etree.tostring(unit.xpath("./td[2]"))
    }

## USA && Canada
    # "stanford.geometry" :"https://geometry.stanford.edu/member/guibas/publications.php",
                                                                                ## Leo Guibas 
}  
