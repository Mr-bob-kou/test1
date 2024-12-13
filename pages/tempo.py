import folium
from folium import IFrame

# 創建地圖
m = folium.Map(location=[51.505, -0.09], zoom_start=13)

# 添加點擊事件
click_event = """
    function(e) {
        alert("You clicked the map at: " + e.latlng);
    }
"""
m.get_root().html.add_child(folium.Element(f"<script>{click_event}</script>"))

# 顯示地圖
m.to_streamlit(height=700)
