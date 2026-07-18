# import csv

# with open("students.csv","w",newline="",encoding="utf-8") as file:

#     writer = csv.writer(file)

#     writer.writerow(["姓名","成績"])

#     while True:

#         name = input("姓名exit:")

#         if name == "exit":
#             break

#         score = float(input("成績:"))

#         writer.writerow([name,score])

# print("處存完成!")


#92題

# import pandas as pd
# df = pd.read_csv("students.csv")

# print(df)

# print(round(df["成績"].mean(),2))
# print(df["成績"].max())
# print(df["成績"].min())

# print("成績大於80")
# print(df["成績"]>80)
# print(df[df["成績"]>80])

# print("尋找名子")
# print(df["姓名"] == "Kyle")
# print(df[df["姓名"] == "Kyle"])

# highest = df["成績"].max()
# print(df[df["成績"] == highest])

# print(df.sort_values("成績",ascending=False))

# df["是否及格"] = df["成績"] >= 60
# print(df)

#93題

# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv("students.csv")

# names = df["姓名"]
# scores = df["成績"]

# plt.figure(figsize=(8,5))
# plt.pie(scores, labels=names, autopct="%1.1f%%")


# plt.title("Student Scores")
# plt.xlabel("Student")
# plt.ylabel("score")

# # for i in range(len(names)):
# #     plt.text(names[i],scores[i],scores[i],ha="center")

# plt.show()

#94題

# import json

# students = [
#     {"name": "Kyle","score": 90},
#     {"name": "Tom","score": 80},
#     {"name": "Amy","score": 95}
# ]

# with open("student.json","w",encoding="utf-8") as file:
#     json.dump(students, file, ensure_ascii=False, indent=4) #json.dump()寫入JSON檔
#-------------------------------------------------------------------
# import json

# with open("student.json","r",encoding="utf-8") as file:
#     students = json.load(file) #讀取JSON檔

# print(students)

# for student in students:
#     print(student["name"],student["score"])
#-------------------------------------------------------------------
# import json
# students = []

# while True:

#     name = input("姓名輸入離開exit:")

#     if name == "exit":
#         break

#     score = float(input("輸入成績:"))

#     students.append({
#         "name":name,
#         "score":score
#     })

# with open("students.json","w",encoding="utf-8") as file:
#     json.dump(students, file, ensure_ascii=False, indent=4)

#--------------------------------------------------------------

# import json
# students = []
# with open("students.json","r",encoding="utf-8") as file:
#     students = json.load(file)

# for student in students:
#     print(student["name"],student["score"])

#95題

# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# data = response.json()

# print(data[0]["name"])
# print(data[0]["email"])

# for user in data:
#     print(user["name"])

#96題
# import requests

# url = "https://api.github.com/users/octocat"
# response = requests.get(url)

# user = response.json()

# print(user)
# print(user["login"])  #資料["鍵"]
# print(user["name"])
# print(user["followers"])
# print(user["following"])
# print(user["public_repos"])

#97題

# import requests

# username = input("GitHub 使用者:")

# url = f"https://api.github.com/users/{username}"

# response = requests.get(url)

# user = response.json()

# print(user["login"])
# print(user["public_repos"])

# if response.status_code == 200:

#     user = response.json()
#     print("帳號:",user["login"])
#     print("公開專案:",user["public_repos"])
#     print("追蹤者:",user["followers"])

# else:
#     print("找不到使用者")


#98題
"""
========== 天氣查詢 ==========
請輸入城市：
Taipei

城市：Taipei
溫度：31°C
濕度：75%
風速：4.2m/s
"""
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=22.6163&longitude=120.3133&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
response = requests.get(url)

data = response.json()
print(data.keys())
print(data["current"])
current = data["current"]

# print("溫度:",current["temperature_2m"])
# print("濕度:",current["relative_humidity_2m"])                  
# print("風速:",current["wind_speed_10m"])

print("溫度:",data["current"]["temperature_2m"])
print("濕度:",data["current"]["relative_humidity_2m"])                  
print("風速:",data["current"]["wind_speed_10m"])