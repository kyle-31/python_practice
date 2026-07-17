# #BMI = Weight / Height ** 2
# user_weight = float(input("請輸入體重:(單位公斤)"))
# user_height = float(input("請輸入身高:(單位公尺)"))

# user_BMI = user_weight / user_height ** 2
# print("your BMI "+str(user_BMI))


# if user_BMI <= 18.5:
#     print("瘦")
# elif 18.5 < user_BMI <= 25:
#     print("正常")
# elif 25 < user_BMI <= 30:
#     print("小胖")
# else:
#     print("胖")


def calculate_BMI(weight,height):
    user_BMI = weight / height ** 2
    if user_BMI <= 18.5:
        category = "瘦"
    elif user_BMI <= 25:
        category = "正常"
    elif user_BMI <= 30:
        category = "偏胖"
    else:
        category = "胖"
    print(f"您的BMI分類為:{category}")
    
    return user_BMI



calculate_BMI(60,1.8)
a = calculate_BMI(60,1.8)  #如果沒有retur user_BMI 
print(a)                   #就會是None 因為函式沒有回傳任何東西，所以 Python 自動回傳 None
calculate_BMI(30,1.9)
calculate_BMI(120,1.6)

