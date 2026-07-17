#定義一個裝飾器1到50總和
def calculate(callback):
    def run():
        #裝飾器想要執行的程式碼
        result = 0
        for n in range(51):
            result += n
        #把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run

@calculate
def show(n):
    print("計算結果是",  n)

show()

# #定義裝飾器

# def Demodeco(callback):
#     def run():
#         print("裝飾器中的程式碼")
#         callback(5) #這個回呼函式就是被裝飾的普通函式
#     return run


# #使用裝飾器
# @Demodeco
# def Demo(n):
#     print("普通函式的程式碼",n)

# Demo()