## 🐍 Python 小筆記

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
- 多行註解：用 `'''   '''` 包起來

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
