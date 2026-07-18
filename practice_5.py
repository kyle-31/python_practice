#41題
# score = [80, 90, 70, 100, 60]
# print(score)

#42題
# score = [80, 90, 70, 100, 60]
# print("第一個成績:",score[0])
# print("第二個成績:",score[2])
# print("第三個成績:",score[-1])

#43題

# number = []
# for i in range(5):
#     n = int(input("輸入:"))
#     number.append(n)
#     i += 1
# print(number)

#44題

# total = 0
# for i in range(5):
#     n = float(input("輸入數字:"))
#     total = total + n
    

# sum_calculate = total / 5

# print(sum_calculate)

#45題
# num_list = []
# for i in range(5):
#     num = float(input("輸入數字:"))
#     num_list.append(num)
# print(max(num_list))

#46題

# num_list = []
# for i in range(5):
#     num = float(input("輸入數字:"))
#     num_list.append(num)
#     
# print(min(num_list))

#47題

# number = [8, 3, 10, 2, 5]
# number.sort()
# print(number)

#48題

# number = [8, 3, 10, 2, 5]
# number.sort(reverse=True)
# print(number)

#49題

# names = ["Kyle" ,"Tom" ,"Amy" ,"John"]

# user_input = str(input("輸入姓名:"))
# if user_input in names:
#     print("找到"+user_input)
# else:
#     print("查無此人")

#50題
# score_list = []
# count = 0
# user_score_input = None

# while user_score_input != -1:
#     user_score_input = float(input("輸入成績:"))
#     if user_score_input == -1:
#         break
#     score_list.append(user_score_input)
#     count += 1


# print("共有" + str(count) + "筆資料")
# print("最高分:" , float(max(score_list)))
# print("最低分" , float(min(score_list)))
# print("平均:" , float((sum(score_list)/count)))
