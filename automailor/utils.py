import time
import json5 as json
import os
from shutil import copyfile
from pathlib import Path

## copy the default in library
def default_config(path:str):
    pwd = Path(__file__).parent.absolute()
    default_send = f"{pwd}/config/config_send.json"
    default_url = f"{pwd}/config/config_url.json"
    if not os.path.exists(path): os.mkdir(path)
    copyfile(default_send, f"{path}/config_send.json")
    copyfile(default_url, f"{path}/config_url.json")
    return f"{path}/config_send.json", f"{path}/config_url.json" 

## read a json
def read_json(path:str):
    with open(path, "r") as file:
        ret = json.load(file)
    return ret

## get dic[keys]
def extra_keys(keys:list, dic:dict):  
    ret = []
    for key in keys: 
        ret.append(dic[key])
    return ret

## unique
def unique(x:list):
    x = list(set(x))
    return x

## get a compact string of time
def get_time()->str: 
    lt = time.localtime()
    return f"{lt.tm_hour}:{lt.tm_min}:{lt.tm_sec}\t{lt.tm_year}/{lt.tm_mon}/{lt.tm_mday}"

## give font(backcolor, font, color) to a string
def font(text:str, color:str, end_color:str='lightgrey'):
    _font_color = dict()
    _font_color['red'] = '\033[31m'
    _font_color['green'] = '\033[32m'
    _font_color['orange'] = '\033[33m'
    _font_color['blue'] = '\033[34m'
    _font_color['purple'] = '\033[35m'
    _font_color['cyan'] = '\033[36m'
    _font_color['darkgrey'] = '\033[90m'
    _font_color['lightred'] = '\033[91m'
    _font_color['lightgreen'] = '\033[92m'
    _font_color['yellow'] = '\033[93m'
    _font_color['lightblue'] = '\033[94m'
    _font_color['pink'] = '\033[95m'
    _font_color['lightcyan'] = '\033[96m'
    _font_color['lightgrey'] = '\033[37m'
    return f"{_font_color[color]}{text}{_font_color[end_color]}"

