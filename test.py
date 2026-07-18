


# import requests
# from pprint import pprint

# url = 'https://api.kcg.gov.tw/Api/Service/Get/b4dd9c40-9027-4125-8666-06bef1756092'

# response = requests.get(url)

# data = response.json()


# print(type(data))
# print(data.keys())
# print(type(data["data"]))
# print(len(data["data"]))
# print(data["data"].keys())
# print(type(data["data"]["data"]))
# print(data["data"]["data"].keys())
# print(type(data["data"]["data"]["retVal"]))
# print(len(data["data"]["data"]["retVal"]))

# from pprint import pprint

# records = data["data"]["data"]["retVal"]

# station = records[0]

# print("站點名稱：", station["sna"])
# print("行政區：", station["sarea"])
# print("地址：", station["ar"])
# print("總車位：", station["tot"])
# print("空車位：", station["bemp"])

# for i in range(5):
#     print(records[i]["sna"])


# for station in records:
#     if station["sarea"] == "新興區":
#         print(station["sna"])


# count = 0

# for station in records:
#     if station["sarea"] == "新興區":
#         count += 1

# print("新興區共有", count, "個 YouBike 站點")




students = ["Kyle", "Tom", "Amy"]
scores = [90, 80, 95]

print(list(zip(students, scores)))