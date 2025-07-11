import streamlit as n
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if "history" not in n.session_state:
    n.session_state.history = []

if "system_message" not in n.session_state:
    n.session_state.system_message = "請用繁體中文進行後續對話"

col1, col2 = n.columns([6, 1])
with col1:
    n.session_state.system_message = n.text_input(
        "系統訊息", n.session_state.system_message
    )
with col2:
    if n.button("💩"):
        n.session_state.history = []
        n.rerun()

for message in n.session_state.history:
    if message["role"] == "user":
        n.chat_message("user", avatar="💀").write(message["content"])
    else:
        n.chat_message("assistant", avatar="🤡").write(message["content"])
prompt = n.chat_input("請輸入想要對話的訊息")
if prompt:
    n.session_state.history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model="gpt-4o-mini-search-preview",
        messages=[{"role": "system", "content": n.session_state.system_message}]
        + n.session_state.history,
    )

    assistant_message = response.choices[0].message.content
    n.session_state.history.append({"role": "assistant", "content": assistant_message})
    n.rerun()
