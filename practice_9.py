#81題
# with open("hello.txt", "w", encoding = "utf-8") as file:
#     file.write("Hello Python")


#82題

# with open("hello.txt" , "r", encoding= "utf-8") as file:
#     content = file.read()
#     print(content)

#83題

# with open("students.txt","w",encoding="utf-8") as file:
#     file.write("Kyle\nTom\nAmy")

# with open("students.txt","r",encoding="utf-8") as file:
#     content = file.read()
    
# print(content)

#84題
# count = 1
# with open("students.txt","r",encoding="utf-8") as file:
#     for line in file:
#         print("第",count,"位",line.strip())
#         count += 1

#85題
# name = input("輸入名子:")

# with open("students.txt","a",encoding="utf-8") as file:
#     file.write("\n"+name)

# print("新增成功")


#86題
# while True:
#     name = input("輸入名子:")
#     if name == "exit":
#         break
#     score = input("輸入成績:")
#     with open("scores.txt","a",encoding="utf-8") as file:
#         file.write(name + "," + score + "\n")

# print("新增成功")


#87題
# scores = []

# with open("scores.txt","r",encoding="utf-8") as file:
#     for line in file:                  #line → "Kyle,90\n"
#         data = line.strip().split(",") #strip() → "Kyle,90"  |  split(",") → ["Kyle", "90"]
#         name = data[0]
#         score = float(data[1])
#         scores.append(score)

# print("共有",len(scores),"筆資料")
# print("平均成績",round(sum(scores)/len(scores),2))
# print(scores)

#88題
# names = []
# scores = []

# with open("scores.txt","r",encoding="utf-8") as file:
#     for line in file:
#         data = line.strip().split(",")
#         name = data[0]
#         score = float(data[1])
#         names.append(name)
#         scores.append(score)

# while True:
#     search_name = input("輸入要查詢名子:")
#     if search_name == "exit":
#         print("結束")
#         break

#     if search_name not in names:
#         print("查無此人")
#     else:
#         student_index = names.index(search_name)
#         print(search_name,"的成績是",scores[student_index])
    


#89題

#73題
"""
做一個待辦事項。

例如：

1. 新增事項
2. 查看事項
3. 刪除事項
4. 離開

例如：

新增：

寫Python

之後：

目前待辦：

1. 寫Python
2. 寫英文
3. 看書
"""


# items = []
# repeat = []
# def NewItems():
#     item = input("輸入新增事項:")
#     if item in items:
#         print("你已輸入過",item)
#     items.append(item)
#     print("新增成功",item)

# def CheckItems():
#     print(items)

# def DeleteItem():
#     item_remove = input("輸入你想刪除的項目:")
#     if item_remove in items:
#         items.remove(item_remove)
#         print("刪除成功")
#     else:
#         print("找不到這個項目")


# while True:
#     print("""
# 1.新增事項
# 2.查看事項
# 3.刪除事項
# 4.離開""")
    
#     choice = input("輸入所需模式1~4:")

#     if choice == "1":
#         NewItems()

#     elif choice == "2":
#         CheckItems()

#     elif choice == "3":
#         DeleteItem()

#     elif choice == "4":
#         print("謝謝使用")
#         break
#     else:
#         print("輸入錯誤")


def LoadItem():         #先準備讀取檔案的函式
    items = []           #每次需要查看或刪除時,都先把todo.txt讀成List

    try:                #第一次執行可能還沒有todo.txt
        with open("todo.txt","r",encoding="utf-8") as file:     #如果直接用"r"讀取會報錯所以用try
            for line in file:                                   #如果找不到檔案 except FileNotFoundError 就先不做任何事等新增第一筆資料時Python自動建立檔案
                item = line.strip()                 

                if item != "":
                    items.append(item)

    except FileNotFoundError:
        pass

    return items

def AddItem():
    item = input("輸入新增事項:").strip()

    if item == "":
        print("事項不能為空白")
        return

    items = LoadItem()

    if item in items:
        print("這個事項已經存在")
        return

    with open("todo.txt","a",encoding="utf-8") as file:     #"a"代表加入檔案最後面不會覆蓋舊資料
        file.write(item + "\n")

    print("新增成功")


def DisplayItem():
    items = LoadItem()

    if len(items) == 0:
        print("目前沒有待辦事項")
        return

    print("\n目前待辦事項:")

    for i in range(len(items)):
        print(i + 1,items[i])       #重0開始所以加一


def DeleteItem():
    items = LoadItem()

    if len(items) == 0:
        print("目前沒有待辦事項")
        return 

    for i in range(len(items)):
        print(i + 1,items[i])

    try:
        number = int(input("輸入要刪除的編號:"))

        if number < 1 or number > len(items):
            print("沒有這個編號")
            return 

    except ValueError:
        print("請輸入整數編號")
        return 


    remove_item = items.pop(number - 1) #假設使用者選1但是List第一個元素是索引是0

    with open("todo.txt","w",encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")

    print("已刪除:",remove_item)


while True:
    print("""
1.新增事項
2.查看事項
3.刪除事項
4.離開
""")

    choice = input("輸入1到4:")

    if choice == "1":
        AddItem()
    elif choice == "2":
        DisplayItem()
    elif choice == "3":
        DeleteItem()
    elif choice == "4":
        print("謝謝使用")
        break
    else:
        print("輸入錯誤")
