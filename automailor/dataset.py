import os
import json5 as json


class Dataset(object):
    def __init__(self, path:str):
        self.path = path

    def write(self, info):
        info = json.dumps(info, indent=4)
        with open(self.path, "w") as file:
            file.write(info)

    def read(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                ret = json.load(file)
            return ret
        else:
            return {}
