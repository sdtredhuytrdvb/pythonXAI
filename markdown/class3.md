## 🧠 今天學到的 Python 小筆記（給國小生看的版本）

---

### 🔢 如果做判斷（像選擇題一樣）

#### 1️⃣ `if`（如果）

👉 如果「這件事是真的」，就做後面的事情。

```python
if 天氣 == "下雨":
    print("記得帶雨傘")
```

#### 2️⃣ `elif`（如果不是那個，那這個呢？）

👉 再檢查另一種可能。

```python
if 成績 >= 90:
    print("你超棒！")
elif 成績 >= 60:
    print("你及格囉～")
```

#### 3️⃣ `else`（其他所有狀況）

👉 如果上面都不是，就做這個。

```python
else:
    print("再加油沒關係！")
```

---

### 🔁 讓電腦做很多次的事情

#### `for i in range(...)`

👉 電腦會「重複做事情」幾次。

```python
for i in range(3):
    print("你好")  # 會印3次
```

你也可以加上開始跟結束的數字：

```python
for i in range(1, 5):
    print(i)  # 印 1 到 4
```

還可以設定跳幾格：

```python
for i in range(1, 10, 2):
    print(i)  # 印奇數：1, 3, 5, 7, 9
```

---

### 📦 列表 List（像一盒裝著很多東西的盒子）

```python
水果 = ["蘋果", "香蕉", "芭樂"]
```

#### 列表的功能們：

✅ `.append(東西)` ➜ 加在最後面
✅ `.remove(東西)` ➜ 把指定的東西刪掉
✅ `.pop()` ➜ 拿出最後一個東西
✅ `.sort()` ➜ 幫東西排順序
✅ `.copy()` ➜ 複製一份新的出來

📌 例子：

```python
水果.append("橘子")  # 加橘子
水果.remove("香蕉")  # 把香蕉移除
新水果 = 水果.copy()  # 複製一份
```

---

### 📖 讀檔案的小技巧

```python
f = open("我的檔案.txt", "r", encoding="utf-8")
內容 = f.read()
print(內容)
f.close()
```

💡 更安全的寫法：

```python
with open("我的檔案.txt", "r", encoding="utf-8") as f:
    內容 = f.read()
    print(內容)
```

---

### 🔚 `.endswith(".xxx")` ➜ 看檔名有沒有這個結尾

```python
檔名 = "筆記.md"
print(檔名.endswith(".md"))  # 看是不是 Markdown 檔
```

---

### 🎈 Streamlit：做互動網頁的小幫手

```python
import streamlit as n

n.write("按鈕練習")

if n.button("按我一下"):
    n.write("你按下去了！")

if n.button("放煙火"):
    n.balloons()

if n.button("下雪囉"):
    n.snow()
```

#### ⛰️ 金字塔練習

輸入一個數字，就會顯示數字金字塔：

```python
t = n.number_input("請輸入數字", min_value=1, max_value=9, step=1)
for i in range(1, t + 1):
    n.write(f"{i}" * i)
```

---

### 🎓 小補充：複製變數的小知識

#### 📍 傳值 (call by value)

```python
a = 1
b = a
b = 2
# a還是1，因為b只是複製它的數字
```

#### 📍 傳參考 (call by reference)

```python
a = [1, 2, 3]
b = a
b[0] = 9
# a也被改成 [9, 2, 3]
```

✅ 如果不想改到原本的，可以這樣：

```python
b = a.copy()  # 這樣改b不會影響a
```

---

### 🧪 其他補充的小例子

```python
print([1, 2, 3] * 3)  # ➜ [1, 2, 3, 1, 2, 3, 1, 2, 3]
print([1, 1.5, "a", True])  # 列表可以放不同類型
```
