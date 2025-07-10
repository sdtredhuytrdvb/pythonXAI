import streamlit as n

n.title("購物籃")

if "order" not in n.session_state:
    n.session_state.order = []
col1, col2 = n.columns(2)
with col1:
    foodinput = n.text_input("請加入餐點")
with col2:
    if n.button("加入購物籃", key="add"):
        n.session_state.order.append(foodinput)
n.write(f"購物籃")
for i in range(len(n.session_state.order)):
    col1, col2 = n.columns(2)
    with col1:
        n.write(n.session_state.order[i])
    with col2:
        if n.button("刪除", key=i):
            n.session_state.order.pop(i)
            n.rerun()
