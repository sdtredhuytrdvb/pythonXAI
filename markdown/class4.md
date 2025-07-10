# 🐍 今天學到的 Python 筆記

## 🔹 1. 我們使用了 `streamlit` 這個工具

這是一個可以幫我們做「網頁小工具」的套件，像是按鈕、文字輸入、顯示內容等等。
就像在寫程式版的互動網頁。

---

## 🔹 2. `欄位元件`：讓畫面有左右兩邊

我們可以用 `n.columns(...)` 來把畫面分成幾欄。

### 🧪 例子：

```python
col1, col2 = n.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

這樣會在畫面左邊出現「按鈕 1」，右邊出現「按鈕 2」。

你也可以分成三欄、四欄，還可以調整欄位比例：

```python
col1, col2, col3 = n.columns([1, 2, 3])
```

---

## 🔹 3. 按鈕（button）

使用 `n.button("按鈕名稱")` 可以讓畫面出現按鈕。
可以加上 `key="名稱"` 來給每個按鈕不同的代號，避免出錯。

---

## 🔹 4. 文字顯示 `n.write()` 和標題 `n.title()`

- `n.write("你想寫的字")` 會在畫面上顯示文字
- `n.title("大標題")` 會顯示比較大的標題字

---

## 🔹 5. `with` 的用法

```python
with col1:
    n.button("我是左邊的按鈕")
```

這樣就可以讓元件出現在某一欄位裡（例如左邊或右邊）。

---

## 🔹 6. 文字輸入 `n.text_input()`

```python
text = n.text_input("請輸入你的名字", value="小明")
n.write(f"你輸入的是：{text}")
```

這會讓你可以在網頁上輸入一段文字，然後顯示出來。

---

## 🔹 7. `session_state`：記住資料

平常按下按鈕後資料會被「重置」，用 `n.session_state` 可以記住變數的值。

```python
if "ans1" not in n.session_state:
    n.session_state.ans1 = 1
```

這段意思是：「如果還沒有 ans1，就設成 1」。

---

## 🔹 8. 🎈 特效 `n.balloons()`

當你按下某個按鈕時可以出現氣球！

```python
if n.button("按我放氣球"):
    n.balloons()
```

---

## 🔹 9. `n.rerun()`：重新整理畫面

這可以讓畫面重新執行一次程式，用在像「刪除」、「更新」這種情況。

---

## 🔹 10. 製作購物籃的小程式 🛒

使用文字輸入和按鈕來新增餐點到購物籃（用 list 存起來），還可以刪除餐點。

```python
if "order" not in n.session_state:
    n.session_state.order = []
```

用 `.append()` 把東西加進購物籃，用 `.pop(i)` 把第 i 個刪掉。

---

# 🔸 程式語法與邏輯部分

## ✅ 變數計算方法

```python
a = 1
a += 1   # 加1
a -= 1   # 減1
a *= 2   # 乘2
a /= 2   # 除2
a //= 2  # 整數除法
a %= 2   # 餘數
a **= 2  # 次方（平方）
```

---

## 🔁 迴圈（重複做的事）

### 🔸 `while` 迴圈

當條件成立時就一直執行，像這樣：

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### 🔸 `for` 迴圈

使用 `range(5)` 就會從 0 到 4（共 5 次）

```python
for i in range(5):
    print(i)
```

---

## ❗ `break`：跳出迴圈

如果你用 `break`，就會停止現在的 `for` 或 `while` 迴圈。

---

## 🎲 隨機數字（random）

```python
import random
print(random.randint(1, 6))        # 隨機 1~6 之間的整數
print(random.randrange(1, 7, 2))   # 1~6，間隔為 2（只出現奇數）
```

---

## 🎮 猜數字遊戲（猜 1\~100 的整數）

```python
ans = random.randint(1, 100)

while True:
    num = int(input("請輸入1~100的整數："))
    if num < 0 or num > 100:
        print("超出範圍")
    elif num > ans:
        print("太大了")
    elif num < ans:
        print("太小了")
    else:
        print("答對了！")
        break



```
