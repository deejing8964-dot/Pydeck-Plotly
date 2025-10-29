import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def app():
    """Plotly 3D 範例頁面（被 `app.py` 呼叫）。"""
    st.title("Plotly 3D 地圖 (向量 - 地球儀)")

    # 1. 載入範例資料
    df = px.data.gapminder().query("year == 2007")

    # 2. 建立地理散點圖
    fig1 = px.scatter_geo(
        df,
        locations="iso_alpha",
        color="continent",
        hover_name="country",
        size="pop",
        projection="orthographic",
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.title("Plotly 3D 地圖 (網格 - DEM 表面)")

    # 讀取範例 DEM 資料 (Mt Bruno)
    z_data = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv"
    )

    # 建立 Surface 圖
    fig2 = go.Figure(
        data=[
            go.Surface(z=z_data.values, colorscale="Viridis"),
        ]
    )
    fig2.update_layout(
        title="Mt. Bruno 火山 3D 地形圖 (可旋轉)",
        width=800,
        height=700,
        scene=dict(xaxis_title="經度 (X)", yaxis_title="緯度 (Y)", zaxis_title="海拔 (Z)"),
    )

    st.plotly_chart(fig2, use_container_width=True)


if __name__ == "__main__":
    app()