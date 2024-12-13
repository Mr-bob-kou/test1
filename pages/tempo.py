import streamlit as st
import leafmap.foliumap as leafmap
import folium
from folium import GeoJson

# 創建一個 Streamlit 頁面
st.title("Leafmap 點擊事件示例")

# 初始化地圖，設置中心和縮放級別
m = leafmap.Map(center=[51.505, -0.09], zoom=13)

# GeoJSON 數據（這裡用一個簡單的示例）
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [51.505, -0.09]
            },
            "properties": {
                "name": "Feature 1",
                "description": "這是圖徵 1"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [51.515, -0.1]
            },
            "properties": {
                "name": "Feature 2",
                "description": "這是圖徵 2"
            }
        }
    ]
}

# 添加 GeoJSON 到地圖
geojson_layer = GeoJson(geojson_data)
geojson_layer.add_to(m)

# 點擊事件處理
def on_click(event):
    lat, lon = event['latlng']
    # 查找被點擊的圖徵，這裡會根據經緯度查找
    clicked_feature = None
    for feature in geojson_data['features']:
        coords = feature['geometry']['coordinates']
        if coords[0] == lat and coords[1] == lon:
            clicked_feature = feature
            break
    if clicked_feature:
        properties = clicked_feature['properties']
        st.write(f"屬性：{properties}")

# 需要將地圖渲染到 Streamlit 中
m.add_child(folium.LatLngPopup())  # 顯示點擊位置

# 顯示地圖
st_map = m.to_streamlit()

# 顯示點擊後的屬性
st.write("點擊地圖上的圖徵來顯示屬性。")
