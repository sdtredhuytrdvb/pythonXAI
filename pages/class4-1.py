import streamlit as n

n.title("欄位元件")

col1, col2 = n.columns(2)
col1.button("button1", key="btn1")
col2.button("button2", key="btn2")

col1, col2 = n.columns(2)
col1.button("button3", key="btn3")
col2.button("button4", key="btn4")

col1, col2, col3 = n.columns([1, 2, 3])
col1.button("button5", key="btn5")
col2.button("button6", key="btn6")
col3.button("button7", key="btn7")

col1, col2 = n.columns([1, 2])
with col1:
    n.write("col1")
col1, col2 = n.columns([1, 2])
with col1:
    n.write("col1")
    if n.button("button8", key="btn8"):
        n.balloons()
with col2:
    n.write("col2")
    n.button("button9", key="btn9")

cols = n.columns(4)
for i in range(4):
    with cols[i]:
        n.button(f"button{i+1}", key=f"多col{i+10}")

n.write("---")
n.title("文字元件")
col1, col2 = n.columns(2)
with col1:
    n.button("button10", key="btn10")
    n.button("button11", key="btn11")
    n.button("button12", key="btn12")
with col2:
    n.write("col2")
    n.write("col2")
    n.write("col2")

n.write("---")
for i in range(3):
    col1, col2 = n.columns(2)
    with col1:
        n.button(f"button{i+1}", key=f"btn.{i+4}")
    with col2:
        n.button(f"btn{i+1}")

n.write("---")
n.title("文字輸入元件")
text = n.text_input("請輸入一個文字", value="這是預設文字")
n.write(f"你輸入的是：{text}")

# session_state
n.write("---")
n.title("session_state")

ans = 1
if n.button("按下去ans+1", key="ans"):
    ans = ans + 1
n.write(f"ans={ans}")

if "ans1" not in n.session_state:
    n.session_state.ans1 = 1

if n.button("按下去ans+1", key="ans2"):
    n.session_state.ans1 = n.session_state.ans1 + 1
n.write(f"ans={n.session_state.ans1}")

if n.button("重新整理畫面", key="abc"):
    n.rerun()
