import streamlit as n
import os

n.title("圖片元件")

n.image("image/banana.png", width=300)

image_folder = "image"
image_files = os.listdir(image_folder)
n.write(image_files)

for image_file in image_files:
    n.image(f"{image_folder}/{image_file}", width=300)

n.write("---")

image_size = n.number_input(
    "請輸入圖片大小", min_value=50, max_value=500, step=50, value=100
)

for image_file in image_files:
    n.image(f"{image_folder}/{image_file}", width=image_size)

for image_file in image_files:
    n.image(f"{image_folder}/{image_file}", use_container_width=True)

selected_image = n.selectbox("選擇要顯示的圖片", image_files)
n.image(f"{image_folder}/{selected_image}", width=500)
