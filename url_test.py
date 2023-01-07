## Note: 一些xpath的坑
## 1. 浏览器会美化html，导致复制出来的xpath会多一个`tbody`标签，应当手动去掉
## 2. 
authors_dict = { 
    ### Germany
    "mpi.andreas_geiger" : {
        "name"               : "Andreas Geiger (Max-Plank-Institute for Information)",
        "url"                : "https://www.cvlibs.net/publications.php", 
        "xpath"              : "/html/body/div[2]/div/div[@class='publication_title']", 
        ## and '/html/body/div[2]/div[@class=publication_detail]'
    },
    "mpi.justus_thies" : {
        "name"              : "Justus Thies (Max-Plank-Institute for Information)",
        "url"               : "https://justusthies.github.io/publications/",
        "xpath"             : "/html/body/div/div/article/div/article/div",
    },
    "mpi.vcai"         :{
        "name"              : "Max-Plank-Institute for Information, Stuggart",
        "url"               : "https://vcai.mpi-inf.mpg.de/VCAI_Projects.html",   ## MPI Stuggart #/html/body/table[2]/tbody/tr[*]/td[2] (year related)
        "xpath"             : "/html/body/table[2]/tr[*]/td[2]"
    },
    "mpi.machael_black" :{
        "name"              : "Michael Black (MPI, Tuebingen)",
        "url"               : "https://ps.is.mpg.de/publications",                ## Michael J Black
        "xpath"             : "/html/body/main/div/div/div/div[2]/div/div[2]/div/div[@class='col-md-9']"
                            # "/html/body/main/div/div/div/div[2]/div/div[2]/div[5]/div[3]/div/div"
    },
    "mpi.gerard_pons-mol":{
        "name"              : "Gerard Pons-Moll (MPI Tuebingen)",
        "url"               : "https://virtualhumans.mpi-inf.mpg.de/publications.html",
        "xpath"             : "/html/body/main/div/div[@class='media-body align-self-center']"
    },
    ### Switherland
    # "eth.igl"            :{
    #     "name"              : "Interactive Geometry Lab (ETHzurich)",
    #     "url"               : "https://igl.ethz.ch/publications/",
    #     "xpath"             : "/html/body/div/div[2]/div[1]/div[@class='alignSmall']"
    # },
    "eth.vlg"            :{
        "name"              : "Interactive Geometry Lab (ETHzurich)",
        "url"               : "https://vlg.inf.ethz.ch/publications/",
        "xpath"             : "/html/body/section[2]/div/div/div[*]/div/div[@class='row gx-0']"
    },

    ### USA
    "google.jon_barron" : {
        "name"               : "Jonathan Barron (Google Research)",
        "url"                : "https://jonbarron.info",
        "xpath"              : "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]",
    },
    "google.ben_mild" : {
        "name"               : "Ben Mildenhall (Google Research)",
        "url"                : "https://bmild.github.io/",
        "xpath"              : "/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]",
    }, # github need proxy
    "stanford.geometry" : {
        "name"               : "Leo Guibas (Stanford)", ## Leo Guibas
        "url"                : "https://geometry.stanford.edu/member/guibas/publications.php",
        "xpath"              : "/html/body/font/table/tr[1]/td/table/tr"
        ## Warning: tbody是浏览器加上去的。。。https://blog.csdn.net/qq_32590631/article/details/76064127
    }, ## might be question of encoding...
    "upenn.lingjieliu"       : {
        "name"               : "Lingjie Liu (UPenn)",
        "url"                : "https://lingjie0206.github.io/",
        "xpath"              : "/html/body/div[2]/section[3]/div/div/div[2]/div/div/div[2]"
    },        
    # "ucsd.sulab"             : {
    #     "name"               : "Hao Su (UCSD)",
    #     "url"                : "https://cseweb.ucsd.edu/~haosu/index.html",
    #     "xpath"              : "//*[@id='papers']/div[*]"
    # },     
    # "cornell.rgblab"         :{
    #     "name"               : "RGB lab (Cornell)",
    #     "url"                : "https://rgb.cs.cornell.edu/papers/",
    #     "xpath"              : "/html/body/div[2]/main/div[2]/article/section[*]/div[@class='excer[t-wrap']"
    #                         #  "/html/body/div[2]/main/div[2]/article/section[3]/div[2]"
    # }                                      
}  
