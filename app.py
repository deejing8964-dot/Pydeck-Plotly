import streamlit as st
from importlib import import_module

# 很多舊範例使用不存在的 st.Page / st.navigation API。
# 這裡改成用側邊欄的 selectbox 做簡單的多頁導航，並且要求每個頁面模組提供一個 app() 函式。

PAGES = {
    "首頁 🏠": "page_home",
    "Plotly 3D 🌏": "page_3dmap-2",
}

st.sidebar.title("導覽")
choice = st.sidebar.selectbox("選擇頁面", list(PAGES.keys()))

module_name = PAGES[choice]
try:
    module = import_module(module_name)
except Exception as e:
    st.error(f"無法載入頁面模組 {module_name}: {e}")
else:
    # 如果模組定義了 app()，呼叫它；否則嘗試以匯入時的行為顯示內容（較不安全）
    if hasattr(module, "app"):
        module.app()
    else:
        st.warning(f"模組 {module_name} 沒有定義 app()，將直接執行模組的頂層程式碼（若有）。")
        # 直接執行模組頂層（匯入時已經執行），此處顯示訊息
        # 若需要更嚴格的行為，請把頁面內容移到 app() 函式中。