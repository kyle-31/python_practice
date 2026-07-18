#BMI = Weight / Height ** 2
user_weight = float(input("請輸入體重:(單位公斤)"))
user_height = float(input("請輸入身高:(單位公尺)"))

user_BMI = user_weight / user_height ** 2
print("your BMI "+str(user_BMI))


if user_BMI <= 18.5:
    print("瘦")
elif 18.5 < user_BMI <= 25:
    print("正常")
elif 25 < user_BMI <= 30:
    print("小胖")
else:
    print("胖")

print("測試Git")
print("這是在 Branch 測試")