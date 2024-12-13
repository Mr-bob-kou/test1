import leafmap
import folium

m = leafmap.Map(center=[51.505, -0.09], zoom=13)

def on_map_click(e):
    print(f"Clicked at: {e.latlng}")

m.on('click', on_map_click)

# 顯示地圖
m
