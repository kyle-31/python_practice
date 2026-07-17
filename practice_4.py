# n = int(input("輸入邊長:"))

# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end="")
    
#     print()
#32題
# n = int(input("輸入邊長:"))

# for i in range(1,n+1):
#     print("*"*i)

#33題
# n = int(input("輸入邊長:"))

# for i in range(n,0,-1):
#     print("*"*i)

#34題
# max_num = int(input("輸入第一個數字:"))

# for i in range(4):
#     number = int(input("輸入數字"))

#     if number > max_num:
#         max_num = number

# print("最大值是", max_num)

#35題

# min_num = float(input("輸入第一個數字"))

# for i in range(4):
#     number = float(input("輸入數字"))
#     if number < min_num:
#         min_num = number

# print("最小值",min_num)

#36題

# goal_list = []

# for i in range(10):
#     number = float(input("輸入數字"))
#     if number % 2 == 0:
#         goal_list.append(number)


# print("偶數有",len(goal_list),"個")

#37題

# for i in range(20):
#     i = i + 1
#     if i % 5 == 0:
#         continue
#     print("不為五的倍數",i)

#38題

# while True: #True永遠都是成立的
#     n = float(input("輸入:"))
#     if n == 0:
#         break #強制結束
        
# print("結束程式")

#39題
# import random
# answer = random.randint(1,100)

# user_input = int(input("輸入數字:"))
# while user_input != answer:
#     if user_input > answer:
#         print("太大")
        
#     else:
#         print("太小")
#     user_input = int(input("輸入數字:"))

# print("猜對了")

#40題

import random
answer = random.randint(1,100)
count = 0

user_input = int(input("輸入數字:"))
count = count + 1
while user_input != answer:
    if user_input > answer:
        print("太大")
    else:
        print("太小")
    user_input = int(input("輸入數字:"))
    count = count + 1

print("猜對了")
print("猜了",count,"次")