# 程式基本用語/常識:
# 程式由上往下運作,以最下面的程式作為最後的結果
# 初始文字為字串
# 基本運算子:
# 運算子運算順序:
# 運算順序:括號->運算子->參數
# 布林值=T/F,T=1,F=0
# str字串,int整數,float浮點數,bool布林值
# 按鍵功能:
# Ctrl + Z = 上一步
# Ctrl + Y = 下一步
# Ctrl + S = 存檔
# Ctrl + Shift + P = 開啟指令面板
# Ctrl + / = 註解(新增/解除)
# Ctrl + Shift + D = 複製行
# Ctrl + Shift + K =刪除行
# # 輸入方式:
# 輸入:input(“???”)
# 輸出:print(“???”)
# 註解:#???(單行),'''???'''(多行註解)
# 變數:??? = "???"

"""
這是多行註解
這邊可以放很多的文字
"""

# 這是單行註解
print("Hello World!")  # print是在終端機顯示文字的指令
# ctrl+? 可以快速註解/取消註解


# 基本型態
print(1)  # int這是整數, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(1.0)  # float 這是浮點數
print(1.234)  # float 這是浮點數
print("apple")  # str 這是字串 "sadasd123125557", '1'
print(True)  # bool 這是布林值 True/False
print(False)  # bool 這是布林值 True/False

# 變數
a = 10  # 新增一個儲存空間並取名為a, "="的功能是將右邊的值10存入左邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改為"apple"
print(a)  # 在終端機顯示a所存的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取商
print(1 % 1)  # 取餘數
print(2**3)  # 次方

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

# 字串運算，+、*
print("apple" + " pen")  # 字串相加
print("apple " * 3)  # 字串乘法

# 練習
print("可以在終端機顯示文字")
print("之前學過的東西也可以印出來")
a = "hello"
b = "world"
print(a + " " + b)

# 字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示
