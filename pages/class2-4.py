import streamlit as n

# st.number_input()可以讓使用者輸入數字
# step = 1可以讓使用者只能輸入整數
# min_value = 0,可以讓使用者輸入的數字不能小於0
# max_value = 100,可以讓使用者輸入的數字不能大於100
number = n.number_input("請輸入一個數字：", step=1, min_value=0, max_value=100)
# 顯示使用者輸入的數字
n.write(f"你輸入的數字是：{number}")

n.write("---")

n.write("練習")

score = n.number_input("Number", step=1, min_value=0, max_value=100)

if score > 89:
    n.write("level A")
elif score > 79:
    n.write("level B")
elif score > 69:
    n.write("level C")
elif score > 59:
    n.write("level D")
elif score < 60:
    n.write("level F")
