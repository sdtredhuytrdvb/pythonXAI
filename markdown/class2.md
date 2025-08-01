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

### 📚 常用功能庫：

```python
from math import *  # 數學相關功能
```

---

## 🧠 函式（Function）小幫手們！

### 🅰️ 大小寫變換：

- `.lower()`：把字變小寫
- `.upper()`：把字變大寫
- `.islower()`：檢查字是不是**全小寫**（對= `True`，錯= `False`）
- `.isupper()`：檢查字是不是**全大寫**（對= `True`，錯= `False`）

---

### 🔢 位置查找：

- `[]`：找字串的某個字（記得第一個是 **0** 喔！）
- `.index("字")`：告訴你這個字出現在第幾位

---

### ✏️ 換字、轉換：

- `.replace("原本的", "要換成的")`：把字換掉
- `str(東西)`：把東西變成文字
- `int(東西)`：把東西變成整數（沒有小數點）
- `float(東西)`：變成小數（會有小數點）

---

### ➕ 數學功能：

- `abs()`：絕對值（不管正負，都變正數）
- `pow(底數, 次方)`：幾的幾次方
- `max(數, 數, ...)`：找出最大值
- `min(數, 數, ...)`：找出最小值
- `round(數字)`：四捨五入（5 以下捨去、6 以上進位）

---

### 🧮 math 圖書館的強大功能：

```python
from math import *
```

- `floor(數字)`：無條件捨去（直接變小）
- `ceil(數字)`：無條件進位（直接變大）
- `sqrt(數字)`：開根號 √
- `type(變數)`：看是什麼類型（例如字串、數字）

---

## 🧪 判斷式（比大小）

### 比較運算子：

| 比較方式 | 說明       |
| -------- | ---------- |
| `==`     | 等於       |
| `!=`     | 不等於     |
| `>`      | 大於       |
| `<`      | 小於       |
| `>=`     | 大於或等於 |
| `<=`     | 小於或等於 |

### 例子：

```python
print(1 == 1)  # True
print(1 != 2)  # True
```

---

## 🤔 邏輯判斷（多條件）

| 運算子 | 說明                         |
| ------ | ---------------------------- |
| `and`  | 而且（都要對，結果才是對）   |
| `or`   | 或是（只要一個對，結果就對） |
| `not`  | 不是（把對變錯，把錯變對）   |

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

- `st.title("標題")` → 顯示大標題
- `st.write("文字")` → 顯示任何內容（包含數字、字串、Markdown）
- `st.text("純文字")` → 顯示純文字
- `st.markdown("Markdown格式")` → 支援 **粗體**、_斜體_、[連結](https://example.com)、程式碼區塊

### 訊息框：

- `st.info("提示訊息")`
- `st.success("成功提示")`
- `st.warning("警告提示")`
- `st.error("錯誤訊息")`

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

## 📌 小提醒：

- 所有括號的用法要小心！像是：

  - 小括號 `()` 是給函式用的
  - 中括號 `[]` 是拿來抓字串裡面的字

- 第一個字是從 **0 開始數！**

---
