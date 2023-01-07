from lxml import etree
# class LabPublications(object):
#     def __init__(self,name:str ,url:str,content_extration:dict) -> None:
        
#         pass

authors_dict = { 
    "mpi.andreas_geiger" : {
        "name"               : "Andreas Geiger (Max-Plank-Institute for Information)",
        "url"                : "https://www.cvlibs.net/publications.php", 
        "xpath"              : "/html/body/div[2]/div/div[@class='publication_title']", ## and '/html/body/div[2]/div[@class=publication_detail]'
    },
    
    "google.jon_barron" : {
        "name"               : "Jonathan Barron (Google Research)",
        "url"                : "https://jonbarron.info",
        "xpath"              : "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]",
    },
    "google.ben_mild" : {
        "name"               : "Ben Mild (Google Research)",
        "url"                : "https://bmild.github.io/",
        "xpath"              : "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]",
    },
    # "stanford.geometry" : {
    #     "url"                : "https://geometry.stanford.edu/member/guibas/publications.php",
    #     "xpath"              : ""
    # }
                                                                                ## Leo Guibas 
}  
