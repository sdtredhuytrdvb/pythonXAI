# 測試:
import math
from math import *

a = "I"
b = "i"
c = b.lower()
print(a.islower())
print(b.islower())
print(c.islower())
d = -3.14159265358
print(floor(d))  # 類似無條件捨去(小數點後面的數字)
print(abs(d))
e = 4
f = 9
g = 16
h = sqrt(e)
i = sqrt(f)
j = sqrt(g)
print(int(h))
print(int(i))
print(int(j))
print(type(a))
print(max(d, e, f, g, h, j))  # 結果為數字,非變數
print(ceil(d))
str(d)
# print(d.index("5"))  # ???
print(round(d))  # 正負數相反
pi = 3.14
r = float(input("請輸入半徑"))
Area = pi * r**2
print(Area)
