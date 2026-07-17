#51題

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# print(total)

#52題

# numbers = [8, 15, 3, 20, 12]
# numbers.sort(reverse=True)
# print(numbers[1])

#53題

# names = ["Kyle", "Tom", "Amy", "John"]

# names.remove(names[1])

# print(names)

#54題

# fruits = ["apple", "banana", "orange"]
# fruit = str(input("水果名:"))
# if fruit in fruits:
#     print("有這個水果")
# else:
#     print("沒有")

#55題

# n = str(input("輸入字串:"))

# print("共有",len(n),"個字元")

#56題

# words = str(input("輸入字串:"))
# count = 0
# for w in words:
#     if w == "a":
#         count += 1
# print("a出現",count,"次")

# #57題
# words = input("輸入:")
# n = (len(words)-1)

# for i in range(n,-1,-1):
#     print(words[i], end="")

#58題

# user_input = input("輸入密碼:")
# length = len(user_input)
# if length >= 8:
#     print("密碼可以使用")
# else:
#     print("密碼太短")


#59題

# numbers = [1,2,3,2,5,3,6,1]
# repeat = []
# for n in numbers:
#     if numbers.count(n) > 1 and n not in repeat:
#         repeat.append(n)

# print(repeat)


#60題

# names = []
# scores = []
# user_name_input = None
# user_score_input = 0

# while True:
#     name = input("姓名:")
#     if name == "exit":
#         break
#     score = float(input("成績:"))
#     names.append(name)
#     scores.append(score)
# for i in range(len(names)):
#     print(names[i], scores[i])
# print(sum(scores)/len(scores))
# print(max(scores))



