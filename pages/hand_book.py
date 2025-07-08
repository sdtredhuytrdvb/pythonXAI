import streamlit as n

with n.expander("Class 1的筆記"):
    n.title(
        ''' 

        ---
        🐍 Python 小筆記

### 🔸 一開始要知道的事

- 程式是 **從上往下** 一行一行執行的。
- 每一行的指令會一步步做，最後會出現結果。
- 如果你看到英文或中文字被包在 `" "` 或 `' '` 裡面，那叫做「**字串**」，就像文字。

---

### ⌨️ 常用按鍵（快速鍵）

- `Ctrl + Z`：回到上一步
- `Ctrl + Y`：重做剛剛的動作
- `Ctrl + S`：存檔（要常存）
- `Ctrl + /`：加上或拿掉註解
- `Ctrl + Shift + D`：複製這一行
- `Ctrl + Shift + K`：刪掉這一行
- `Ctrl + Shift + P`：開啟指令選單

---

### 🗣️ 印出東西（輸出）

```python
print("Hello World!")
```

用 `print()` 可以把東西顯示在畫面上。

---

### 📥 讓使用者輸入東西

```python
input("請輸入你的名字：")
```

用 `input()` 可以讓別人打字，我們可以把它存起來。

---

### 🧠 註解（讓電腦不執行這行）

- 單行註解：用 `#` 開頭
- 多行註解：用 `"""
    """` 包起來

---

### 🔤 資料的種類（型態）

```python
print(1)         # 整數 int
print(1.5)       # 小數 float
print("apple")   # 文字 str
print(True)      # 布林值 bool：只有 True（真）或 False（假）
```

---

### 📦 變數（像一個資料箱）

```python
a = 10
print(a)

a = "apple"
print(a)
```

- `a = 10` 表示我們把數字 10 放進變數 a。
- `a = "apple"` 也可以把文字放進去，變數就像「裝東西的箱子」。

---

### ➕ 基本的算數

```python
print(1 + 1)   # 加法
print(2 - 1)   # 減法
print(3 * 2)   # 乘法
print(4 / 2)   # 除法
print(5 // 2)  # 取整數商（只要前面的整數）
print(5 % 2)   # 取餘數（剩下的）
print(2 ** 3)  # 次方（2的3次方 = 8）
```

---

### 🥇 計算順序（誰先算？）

1. `()` 先算括號
2. `**` 次方
3. `* / // %` 乘、除、取整數商、取餘數
4. `+ -` 加、減

---

### ✨ 字串的加法和乘法

```python
print("apple" + " pen")   # 字串相加，變成 "apple pen"
print("apple " * 3)       # 重複字串，變成 "apple apple apple "
```

---

### 🧩 f 字串（把變數放進句子裡）

```python
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")
```

這樣可以讓變數直接出現在句子中，非常方便！

---

### ✅ 小練習

```python
a = "hello"
b = "world"
print(a + " " + b)
```

結果會是：`hello world`
'''
    )
with n.expander("Class 2的筆記"):
    n.title(
        """
---

# 🐍【今天學到的 Python 知識筆記】✨

---

## 🏛 圖書館（功能庫）是什麼？

在 Python 裡，有些功能一開始不會自動出現，要「叫出來」才能用，我們叫它們 **功能庫（Library）** 或 **圖書館**！

### 怎麼使用？

```python
import 功能庫名稱
from 功能庫名稱 import 想用的功能
import 功能庫名稱 as 短名字
```

### 📚常用功能庫：

```python
from math import *  # 數學相關功能
```

---

## 🧠 函式（Function）小幫手們！

### 🅰️ 大小寫變換：

* `.lower()`：把字變小寫
* `.upper()`：把字變大寫
* `.islower()`：檢查字是不是**全小寫**（對= `True`，錯= `False`）
* `.isupper()`：檢查字是不是**全大寫**（對= `True`，錯= `False`）

---

### 🔢 位置查找：

* `[]`：找字串的某個字（記得第一個是 **0** 喔！）
* `.index("字")`：告訴你這個字出現在第幾位

---

### ✏️ 換字、轉換：

* `.replace("原本的", "要換成的")`：把字換掉
* `str(東西)`：把東西變成文字
* `int(東西)`：把東西變成整數（沒有小數點）
* `float(東西)`：變成小數（會有小數點）

---

### ➕ 數學功能：

* `abs()`：絕對值（不管正負，都變正數）
* `pow(底數, 次方)`：幾的幾次方
* `max(數, 數, ...)`：找出最大值
* `min(數, 數, ...)`：找出最小值
* `round(數字)`：四捨五入（5以下捨去、6以上進位）

---

### 🧮 math 圖書館的強大功能：

```python
from math import *
```

* `floor(數字)`：無條件捨去（直接變小）
* `ceil(數字)`：無條件進位（直接變大）
* `sqrt(數字)`：開根號 √
* `type(變數)`：看是什麼類型（例如字串、數字）

---

## 🧪 判斷式（比大小）

### 比較運算子：

| 比較方式 | 說明    |
| ---- | ----- |
| `==` | 等於    |
| `!=` | 不等於   |
| `>`  | 大於    |
| `<`  | 小於    |
| `>=` | 大於或等於 |
| `<=` | 小於或等於 |

### 例子：

```python
print(1 == 1)  # True
print(1 != 2)  # True
```

---

## 🤔 邏輯判斷（多條件）

| 運算子   | 說明             |
| ----- | -------------- |
| `and` | 而且（都要對，結果才是對）  |
| `or`  | 或是（只要一個對，結果就對） |
| `not` | 不是（把對變錯，把錯變對）  |

---

## 🥇 計算順序（誰先算？）

1. 括號 `()`
2. 次方 `**`
3. 乘除 `* / // %`
4. 加減 `+ -`
5. 比較 `== != > < >= <=`
6. `not`
7. `and`
8. `or`

---

## 🧾 條件判斷 if

```python
password = input("請輸入密碼：")
if password == "1234":
    print("密碼正確")
elif password == "0000":
    print("這是備用密碼")
else:
    print("密碼錯誤")
```

---

## 🖼 Streamlit 畫面工具（可以做小網頁！）

```python
import streamlit as st
```

### 常用功能：

* `st.title("標題")` → 顯示大標題
* `st.write("文字")` → 顯示任何內容（包含數字、字串、Markdown）
* `st.text("純文字")` → 顯示純文字
* `st.markdown("Markdown格式")` → 支援 **粗體**、*斜體*、[連結](https://example.com)、程式碼區塊

### 訊息框：

* `st.info("提示訊息")`
* `st.success("成功提示")`
* `st.warning("警告提示")`
* `st.error("錯誤訊息")`

---

## 🔢 Streamlit 數字輸入與分數等級顯示

```python
score = st.number_input("請輸入分數：", step=1, min_value=0, max_value=100)

if score > 89:
    st.write("Level A")
elif score > 79:
    st.write("Level B")
elif score > 69:
    st.write("Level C")
elif score > 59:
    st.write("Level D")
else:
    st.write("Level F")
```

---

## 📌小提醒：

* 所有括號的用法要小心！像是：

  * 小括號 `()` 是給函式用的
  * 中括號 `[]` 是拿來抓字串裡面的字
* 第一個字是從 **0 開始數！**

---
"""
    )
