import re
import difflib

class Publications(object):
    def __init__(self, pub_url):
        self.pub_url = pub_url
        pass

    def get_papers(self):
        paper = {
            "paper_name" : {   
                "conference" : "CoRL 2022",
                "name" : "PlanT: Explainable Planning Transformers via Object-Level Representations",
                "authors" : "K. Renz, K. Chitta, O. Mercea, A. Koepke, Z. Akata and A. Geiger",
            },
            ## andreas geiger: 
            #   paper_name.xpath = './/div[@class="publication_title"]/b/text()', 
            #   paper_conference.xpath = './/div[@class="publication_title"]/text()' [1::2]
            #   paper_conference.xpath = './/div[@class="publication_title"]/text()' [::2]
            
            # "abstract" : "Planning an optimal route in a complex environment requires efficient reasoning about the surrounding scene. While human drivers prioritize important objects and ignore details not relevant to the decision, learning-based planners typically extract features from dense, high-dimensional grid representations of the scene containing all vehicle and road context information. In this paper, we propose PlanT, a novel approach for planning in the context of self-driving that uses a standard transformer architecture. PlanT is based on imitation learning with a compact object-level input representation. With this representation, we demonstrate that information regarding the ego vehicle's route provides sufficient context regarding the road layout for planning. On the challenging Longest6 benchmark for CARLA, PlanT outperforms all prior methods (matching the driving score of the expert) while being 5.3x faster than equivalent pixel-based planning baselines during inference. Furthermore, we propose an evaluation protocol to quantify the ability of planners to identify relevant objects, providing insights regarding their decision making. Our results indicate that PlanT can reliably focus on the most relevant object in the scene, even when this object is geometrically distant.",
            "pdf_link" : "https://www.cvlibs.net/publications/Renz2022CORL.pdf",
            ## andreas geiger:
            #   
            "project_link" : "https://www.katrinrenz.de/plant/"
        }
    def make_email_content(self):
        pass
        
# /html/body/table/tbody/tr/td/table[8]/tbody/tr/td/div
# /html/body/table/tbody/tr/td/table[8]/tbody/tr