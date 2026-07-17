english_dict = {"a few":"幾個;為數不多的;有一些(後面接可數名詞)",
                "a little":"少量的(地),稍許的(地)(後面接不可數名詞)",
                "a lot":"【口】大量的,許多的",
                "able":"能,可,會[F][+to-v]"}
english_dict["about"] = "關於,對於"

query = input("輸入查詢的英文單字")
if query in english_dict:
    print("您輸入的單字 " + query + " 含意如下")
    print(english_dict[query])
else:
    print("您輸入的詞不在裡面")
    print("我們收錄的詞為" + str(len(english_dict)) + "個詞")