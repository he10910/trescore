from classes import *

load_setting()

while True:
    num = input("座號(0 ===> 停止輸入):")
    if num == "0":
        print(jdata["student"])
        dump_setting()
        break
    name = input("姓名:")
    try:
        jdata["student"][num] = name
    except:
        error()