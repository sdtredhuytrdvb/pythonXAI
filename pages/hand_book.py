import streamlit as n
import os

folderPath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderPath)  # 取得資料夾內所有檔案
print(files)

files.sort()  # 將清單排序,預設是由小到大

for f in files:
    with open(f"{folderPath}\{f}", "r", encoding="utf-8") as file:
        content = file.read()
        with n.expander(f[:-3]):  # 使用expander,標題為檔案名稱去掉.md
            n.write(content)  # 將檔案內容顯示在網頁上
