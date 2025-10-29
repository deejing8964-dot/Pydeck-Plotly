import streamlit as st
import runpy
import os

# 定義頁面列表（標題、圖示、檔案名稱）
PAGES = [
    {"title": "專案首頁", "icon": "🏠", "file": "page_home.py"},
    {"title": "Pydeck 3D互動地圖瀏覽", "icon": "🌏", "file": "page_3dmap-1.py"},
    {"title": "Plotly 3D互動地圖瀏覽", "icon": "ℹ️", "file": "page_3dmap-2.py"},
]

st.set_page_config(page_title="3D GIS 專案", layout="wide")

with st.sidebar:
    st.title("關於我：自我介紹")
    options = [f"{p['icon']} {p['title']}" for p in PAGES]
    selected = st.selectbox("選擇頁面", options)

# 取得選擇頁面的檔案路徑
selected_index = options.index(selected)
page_info = PAGES[selected_index]
base_dir = os.path.dirname(__file__)
page_path = os.path.join(base_dir, page_info["file"])

# 執行被選擇的頁面
if not os.path.exists(page_path):
    st.error(f"找不到頁面檔案：{page_info['file']}")
else:
    try:
        # 使用 runpy.run_path 執行選定的頁面檔案，讓該檔案內的 Streamlit 程式碼被執行
        runpy.run_path(page_path, run_name="__main__")
    except Exception as e:
        st.error(f"載入頁面時發生錯誤：{e}")