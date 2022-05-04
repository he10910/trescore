from classes import *

load_setting()

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
        
    for num in jdata["student"].keys():
        while True:
            score = input("{},{}的{}成績:".format(num,jdata["student"][num],chi))
            try:
                int(score)
                jdata["score"][sub][num] = score
                dump_setting()
                break
            except:
                error()
    print(jdata["score"][sub])
    input("按Enter回主選單")
    
score("3")