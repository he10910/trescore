from classes import *

load_setting()

numbers = jdata["student"].keys()
scores = jdata["score"]

def sum(num):
    
    sum = 0
    for sub in scores.keys():
        sum += int(scores[sub][num])
    return sum

def average(num):
    
    s = sum(num)
    return s/len(scores.keys())

for num in numbers:
    
    name = jdata["student"][num]
    
    print("{:<5}:".format(name))
    print("國文:{:>3}".format(scores["chinese"][num]),end="")
    print("英文:{:>3}".format(scores["english"][num],end=""))
    print("數學:{:>3}".format(scores["math"][num],end=""))
    print("總分:{:>3},".format(sum(num)),end="")
    print("平均:{:5.2f}".format(average(num)))
    