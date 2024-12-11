import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

# 創建地圖
m = leafmap.Map(center=[40.7128, -74.0060], zoom=12)

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

# 添加GeoJSON圖層到地圖
m.add_geojson(geojson_data)

# 在Streamlit中顯示地圖並捕獲用戶的點擊
clicked_feature = m.to_streamlit(height=700)

# 檢查 clicked_feature 是否存在且包含期望的屬性
if clicked_feature is not None and 'properties' in clicked_feature:
    st.subheader("點擊的要素屬性")
    st.write(f"名稱: {clicked_feature['properties'].get('name', '未提供名稱')}")
    st.write(f"座標: {clicked_feature['geometry'].get('coordinates', '未提供座標')}")
    st.write(f"介紹: {clicked_feature['properties'].get('description', '未提供介紹')}")
else:
    st.write("請點擊地圖上的一個點以查看其屬性資料。")
