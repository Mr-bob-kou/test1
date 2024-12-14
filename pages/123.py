import streamlit as st
import leafmap.foliumap as leafmap
import folium
from folium import GeoJson
import geopandas as gpd
m = leafmap.Map(center=[51.505, -0.09], zoom=13)

# 添加一個標記
marker = m.add_marker([51.505, -0.09], popup="Hello, world!")

# 定義回調函數，當用戶點擊標記時執行
def on_marker_click(event):
    popup_content = event['popup']  # 獲取點擊的標記內容
    print(f"Marker clicked! Popup content: {popup_content}")

# 註冊回調函數以處理標記點擊事件
m.on_interaction(on_marker_click)

# 顯示地圖
m.to_streamlit(width=700)
