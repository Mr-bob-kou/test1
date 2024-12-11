import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium
from folium.features import GeoJsonPopup, GeoJsonTooltip

# 創建地圖
m = folium.Map(location=[35.3, -97.6], zoom_start=4)

# 創建一個範例GeoJSON數據，其中每個點包含座標、名稱和介紹
data = pd.DataFrame({
    'name': ['Point A', 'Point B', 'Point C'],
    'latitude': [40.7128, 40.730610, 40.748817],
    'longitude': [-74.0060, -73.935242, -73.985428],
    'description': ['Description of Point A', 'Description of Point B', 'Description of Point C']
})

# 將數據轉換為GeoJSON格式
geojson_data = {
    "type": "FeatureCollection",
    "features": []
}

for index, row in data.iterrows():
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['longitude'], row['latitude']]
        },
        "properties": {
            "name": row['name'],
            "description": row['description']
        }
    }
    geojson_data['features'].append(feature)

# 創建GeoJsonPopup和GeoJsonTooltip
popup = GeoJsonPopup(
    fields=["name", "description"],
    aliases=["Name:", "Description:"],
    localize=True,
    labels=True,
    style="background-color: yellow;"
)

tooltip = GeoJsonTooltip(
    fields=["name"],
    aliases=["Name:"],
    localize=True,
    sticky=False,
    labels=True,
    style="background-color: #F0EFEF; border: 2px solid black; border-radius: 3px; box-shadow: 3px;"
)

# 添加GeoJson到地圖
folium.GeoJson(
    geojson_data,
    tooltip=tooltip,
    popup=popup
).add_to(m)

# 添加地圖到Streamlit
return_on_hover = st.checkbox("Return on hover?", True)

output = st_folium(m, width=700, height=500, return_on_hover=return_on_hover)

left, right = st.columns(2)
with left:
    st.write("## Tooltip")
    st.write(output["last_object_clicked_tooltip"])
with right:
    st.write("## Popup")
    st.write(output["last_object_clicked_popup"])
