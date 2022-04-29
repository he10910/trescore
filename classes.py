import json

with open("setting.json" , "r" , encoding="utf-8") as jfile:
    jdata = json.load(jfile)

def load_setting():
    with open("setting.json" , "r" , encoding="utf-8") as jfile:
        jdata = json.load(jfile)

def dump_setting():
    with open("setting.json" , "w" , encoding="utf-8") as jfile:
        json.dump(jdata,jfile,indent=4)

def error():
    print(jdata["message"]["error"])