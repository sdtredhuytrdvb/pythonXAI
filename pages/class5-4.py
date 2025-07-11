import streamlit as n

n.chat_message("user").write("這是使用者的訊息")
n.chat_message("assistant").write("這是AI的回應")

history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "哈囉!有什麼我可以可以幫忙得嗎?"},
    {"role": "user", "content": "請問 n.chat_message()怎麼用?"},
    {
        "role": "assistant",
        "content": "n.chat_message()可以讓你用聊天泡泡的方式顯示訊息喔",
    },
]

for message in history:
    if message["role"] == "user":
        n.chat_message("user", avatar="💀").write(message["content"])
    else:
        n.chat_message("assistant", avatar="🤡").write(message["content"])
