#71題

# balance = 10000 #給餘額一個值空間**在之後這個balance會一直改變**


# def CheckBalance():  #定義查詢餘額
#     return balance   #返回balance

# def Deposit(balance, deposit): #定義存款
#     return balance + deposit   #反回餘額加存款

# def Withdrawal(balance, withdrawal): #定義提款
#     if withdrawal > balance:         #如果提款大於餘額列印餘額不足反回餘額
#         print("餘額不足")
#         return balance
#     else:                            #提款小於餘額可以提款所以回傳餘額減提款
#         return balance - withdrawal


# while True:                          #while循環直到選擇4結束
#     print("1. 查詢餘額")
#     print("2. 存款")
#     print("3. 提款")
#     print("4. 離開")
    
#     choice = int(input("輸入數字選擇:"))

#     if choice == 4:
#         print("感謝使用 ATM")
#         break

#     elif choice == 1:
#         print("目前餘額", CheckBalance())  #調用確認餘額函數

#     elif choice == 2:
#         deposit = float(input("存入數字:"))  #輸入存款金額
#         balance = Deposit(balance, deposit) #餘額存入存款函數 balance + deposit
#         print("目前餘額",balance)

#     elif choice == 3:
#         withdrawal = float(input("提款數字:")) #輸入提款金額
#         balance = Withdrawal(balance, withdrawal) #餘額存入提款函數 balance - withdrawal
#         print("目前餘額",balance)

#     else:
#         print("輸入錯誤")





#72題

"""
你以前寫過猜數字。

現在加入：

猜幾次
猜過哪些數字(List)
重複猜提醒

例如：

你猜過：

10
30
55
80
"""
# import random 
# answer = random.randint(1,100)
# count = 0
# repeat = []
# user_input = 0

# while True:
#     user_input = int(input("請猜1~100數字:"))

#     if user_input in repeat:
#         print("你已猜過", user_input)
#         continue

#     repeat.append(user_input)
#     count += 1

#     if user_input > answer:
#         print("太大")
#     elif user_input < answer:
#         print("太小")
#     else:
#         print(" 猜中了")
#         print(f"你已猜過{count}次")
#         print(f"你猜過的數字",repeat)
        
#         break


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



#74題
# 學生管理系統

# students = []

# scores = []


# def AddNewStudent():
#     add_student = input("輸入要新增的學生:")
#     add_score = float(input("輸入此學生成績:"))
#     if add_student in students:
#         print("已經輸入過",add_student,"了")
#     else:
#         students.append(add_student)
#         scores.append(add_score)
#         print("新增成功")

# def CheckAll():
#     for i in range(len(students)):
#         print(students[i], scores[i])

# def CheckTheHighestScore():
#     if len(scores) == 0:
#         print("目前沒有資料")
#     else:
#         highest = max(scores)
#         highest_scores_id = scores.index(highest)
#         print(students[highest_scores_id],max(scores))
    

# def Average():
#     if len(scores) == 0:
#         print("目前沒有資料")
#     else:
#         average = round(sum(scores) / len(students), 2)
#         print(average)


# while True:
#     print("""
# 1. 新增學生
# 2. 查看全部
# 3. 查詢最高分
# 4. 平均
# 5. 離開""")
#     choice = input("輸入選擇1~5:")
#     if choice == "1":
#         AddNewStudent()

#     elif choice == "2":
#         CheckAll()

#     elif choice == "3":
#         CheckTheHighestScore()

#     elif choice == "4":
#         Average()

#     elif choice == "5":
#         print("謝謝使用")
#         break

#     else:
#         print("輸入錯誤")



# 75題
# students = []
# scores = []


# while True:
#     student = input("輸入學生姓名:(結束請打exit):")
#     if student == "exit":
#         print("結束")
#         break
#     else:
#         score = float(input("輸入學生成績:"))
#         students.append(student)
#         scores.append(score)

# for i in range(len(students)):
#     print(students[i],scores[i])


# def ScoreRanking():
#     student_scores = list(zip(students , scores)) #[('Kyle', 90), ('Tom', 80), ('Amy', 95)]
#     student_scores.sort(key=lambda x: x[1], reverse=True) #x[0] → "Kyle" x[1] → 90

#     for student, score in student_scores:
#         print(student, score)

# ScoreRanking()


#76題

# account = "admin"
# password = "1234"
# count = 0

# while True:
#     user_account_input = input("輸入您的帳號:")
#     user_password_input = input("輸入您的密碼:")
#     count += 1

#     if count == 3:
#         print("鎖定")
#         break
#     if user_account_input == account and user_password_input == password:
#         print("登入成功")
#         break
#     else:
#         print("再輸入一次")


#77題
#通訊錄

# contacts = []
# contacts_phone = []


# def AddNewContact():
#     while True:
#         add_contact = input("新增聯絡人(離開exit):")
#         if add_contact == "exit":
#             break
#         add_contact_phone = input("輸入手機號碼:")
#         if add_contact in contacts or add_contact_phone in contacts_phone:
#             print("兩者重複或其中一項重複")
#             print("重新輸入")
#         else:
#             contacts.append(add_contact)
#             contacts_phone.append(add_contact_phone)
#             print("新增成功")


        
# def Research():
#     name = input("輸入要查詢的聯絡人:")
#     if name in contacts:
#         index = contacts.index(name)
#         print(contacts[index] , contacts_phone[index])
#     else:
#         print("查無此人")

# def Delete():
#     delete_contact = input("輸入要刪除姓名:")
#     if delete_contact in contacts:
#         index = contacts.index(delete_contact)
#         contacts.pop(index)
#         contacts_phone.pop(index)
#         print("刪除成功")
#     else:
#         print("無此人刪除")

# def DisplayAll():
#     for i in range(len(contacts)):
#         print(contacts[i], contacts_phone[i])


# while True:
#     print("""
# 1.新增聯絡人
# 2.查詢
# 3.刪除
# 4.列出全部
# 5.離開
# """)

#     choice = input("輸入選擇:")
#     if choice == "1":
#         AddNewContact()
#     elif choice == "2":
#         Research()
#     elif choice == "3":
#         Delete()
#     elif choice == "4":
#         DisplayAll()
#     elif choice == "5":
#         print("謝謝使用")
#         break

#     else:
#         print("輸入錯誤")

#78題
#剪刀石頭布
# import random
# choices = ["剪刀","石頭","布"]

# computer = random.choice(choices)

# while True:
#     user_input = input("輸入剪刀石頭布:")
#     if user_input not in choices:
#         print("輸入錯誤")
#         continue
    
#     break

# print("你出",user_input)
# print("電腦",computer)

# if user_input == computer:
#     print("平手")

# elif (user_input == "剪刀" and computer == "布") or \
#      (user_input == "石頭" and computer == "剪刀") or \
#      (user_input == "布"   and computer == "石頭"):
#      print("你贏了")
# else:
#     print("電腦贏了")   

#79題
# def Square(number):
#     return number ** 2

# def SquareRoot(number):
#     return number ** (1 / 2)

# def Power(number):
#     power = float(input("輸入次方:"))
#     return number ** power

# def Percentage(number):
#     percentage = float(input("輸入百分比:"))
#     return number * percentage / 100

# while True:
#     print("""
# 1. 平方
# 2. 開根號
# 3. 次方
# 4. 百分比
# 5. 離開
# """)
    
#     choice = input("輸入1到4選擇:")

#     if choice == "5":
#         print("謝謝使用")
#         break

#     if choice not in ["1","2","3","4"]:
#         print("輸入錯誤")
#         continue
    
#     number = float(input("輸入要計算的數字:"))
    
#     if choice == "1":
        
#         print(Square(number))
#     elif choice == "2":
        
#         print(SquareRoot(number))
#     elif choice == "3":
        
#         print(Power(number))
#     elif choice == "4":
        
#         print(Percentage(number))
    
#80題

# 查看書籍

# 借書

# 還書

# 離開


books = ["Python","C++","Java","AI"]
status = ["可借閱","可借閱","可借閱","可借閱"]



def DisplayBooks():
    for i in range(len(books)):
        print(books[i],status[i])

def Borrow():
    book_name = input("輸入要借的書名:") 
    if book_name not in books: 
        print("找不到這本書") 
    else: 
        book_index = books.index(book_name) 
        if status[book_index] == "已借出": 
            print("這本書已被借走") 
        else:
            status[book_index] = "已借出" 
            print("借書成功")
def Return():
    book_name = input("輸入要歸還的書名:")
    if book_name not in books:
        print("此書不是本館")

    else:
        book_index = books.index(book_name)

        if status[book_index] == "已借出":
            status[book_index] = "可借閱"

        else:
            print("尚未被借走")



while True:

    print("""
1查看書籍
2借書
3還書
4離開
    """)
    choice = input("輸入1到4選擇")
    

    if choice == "1":
        DisplayBooks()
    elif choice == "2":
        Borrow()
    elif choice == "3":
        Return()
    elif choice == "4":
        print("謝謝使用")
        break
    else:
        print("輸入錯誤")
        