print("這是一個計算平均值的程式")

count = 0
total = 0

user_input = input("輸入數字按q終止程式")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    result = total / count
    user_input = input("輸入數字按q終止程式")
    
if count == 0:
    result = 0
else:
    result = total / count

print("您輸入的平均值為" + str(result))