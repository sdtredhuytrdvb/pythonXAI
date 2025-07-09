import streamlit as n

n.write("按鈕練習")

if n.button("別按我", key="btn1"):
    n.write("戳三小")
if n.button("按爆我", key="btn2"):
    n.balloons()
if n.button("按爛我", key="btn3"):
    n.snow()

n.write("---")

n.write("金字塔桑")

t = n.number_input("Number", min_value=1, max_value=9, step=1)
for i in range(1, t + 1):
    n.write(f"{i}" * i)  # ***
