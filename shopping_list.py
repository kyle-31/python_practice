shopping_list = []
shopping_list.append("鍵盤")
shopping_list.append("鍵帽")
shopping_list.remove("鍵帽")
shopping_list.append("電競椅")
shopping_list.append("音響")
shopping_list[1] = "桌子"

# print(shopping_list)
# print(len(shopping_list))

# print(shopping_list[2])

price = [515 , 6544 , 898 , 423]

max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)

print(max(price))
print(min(price))
print(sorted(price))