from classes import *

load_setting()

{"1":"chinese", \
 "2":"english", \
 "3":"math"} 

def score(num):
    if num == "1":
        sub = "chinese"
        chi = "國文"
    if num == "2":
        sub = "english"
        chi = "英文"
    if num == "3":
        sub = "math"
        chi = "數學"
        
    for key,value in jdata["student"].keys(),jdata["student"].values():
        while True:
            score = input("{},{}的{}成績:".format(key,value,chi))
            try:
                int(score)
                jdata["score"][sub][key] = score
                dump_setting()
                break
            except:
                error()
    print(jdata["score"][sub])
    
score("1")