import streamlit as n

if "history" not in n.session_state:
    n.session_state.history = []

for message in n.session_state.history:
    n.chat_message("user", avatar="☠").write(message["content"])

prompt = n.chat_input("請輸入訊息")
if prompt:
    n.session_state.history.append({"role": "user", "content": prompt})
    n.rerun()
