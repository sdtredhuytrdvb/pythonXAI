import streamlit as n
import streamlit as st

n.title("Sreamlit基本介紹")

import streamlit as st

st.write("> Markdown 語法基本介紹")
st.title("這是標題")
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
```python
print("Hello, Streamlit!")
```
"""
)
st.write("# 在這一堂課當中主要會使用 `st.write`來顯示所有內容。")
st.info("這是一個用 `st.info` 顯示的資訊性文字。")
st.success("這是一個用 `st.success` 顯示的成功訊息。")
st.warning("這是一個用 `st.warning` 顯示的警告訊息。")
st.error("這是一個用 `st.error` 顯示的錯誤訊息。")
