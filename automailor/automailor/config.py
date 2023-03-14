import os
from .utils import read_json

class Config(object):
    def __init__(self, config_path:str="None"):
        if config_path != "None":
            self.load_json(config_path)
        pass

    def dict(self):
        return dict(self.__dict__.items())

    def load_json(self, path:str):
        js_dict = read_json(path)
        for key in js_dict.keys():
            setattr(self, key, js_dict[key])
        return js_dict

    def save_json(self, path:str):
        info = json.dumps(self.dict(), indent=4)
        with open(path, "w") as file:
            file.write(info)
        pass
