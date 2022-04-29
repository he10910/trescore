from classes import *

def menu():
    print("Class 101 班級成績管理系統")
    print()
    print("-"*10)
    print("1. 輸入學生姓名")
    print("2. 輸入國文成績")
    print("3. 輸入英文成績")
    print("4. 輸入數學成績")
    print("5. 顯示成績單")
    print("0. 結束程式")
    print()
    print("-"*10)
    while True:
        a = input("請輸入您的選擇:")
        try:
            a = int(a)
            if a in range(6):
                return a
            else:
                error()
        except:
            error()