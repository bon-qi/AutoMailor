import json

class DatasetJS(object):
    def __init__(self, path:str):
        self.path = path

    def write(self, info):
        info = json.dumps(info, indent=4)
        with open(self.path, "w") as file:
            file.write(info)

    def read(self):
        try:
            with open(self.path, "r") as file:
                ret = file.read()
            ret  = json.loads(ret)
            return ret
        except:
            return {}

    def compare(self, info):
        info_old = self.read()