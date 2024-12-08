import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")


st.title("General")
data="https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/point.geojson"
regions = "https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/world-administrative-boundaries.geojson"
data2="https://github.com/Mr-bob-kou/My_Respository/raw/main/World%20Heritage%20Counts.geojson"

options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")
modes=["Default","Heat Map","Choropleth Map(Count by every Countries)"]
modes1="Default"
def style_function(feature):
    count = feature['properties']['count']
    
    if count > 40:
        color = '#003D79'
    elif count > 30:
        color = "#0066CC"
    elif count > 20:
        color = '#0080FF'
    elif count > 10:
        color = '#C4E1FF'
    else:
        color = '#ECF5FF'
    
    return {
        'fillColor': color,
        'color':"black",
        'weight': 2,
        'fillOpacity': 1
    }
with st.expander("See All Heritage Data"):
    heritage=gpd.read_file(data)
    st.dataframe(data=heritage)
col1, col2 = st.columns([4, 1])


with col2:
    basemap = st.selectbox("Select a basemap:", options, index)
    mode=st.selectbox("Select a Mode",modes)
with col1:
    m = leafmap.Map(center=[40, -100], zoom=4)
    if mode=='Choropleth Map(Count by every Countries)':
        m = leafmap.Map(center=[40, -100], zoom=4)
        m.add_basemap(basemap)
        m.add_geojson(data2,style_callback=style_function)
        m.to_streamlit(height=700)
    elif mode=='Heat Map':
        m = leafmap.Map(center=[40, -100], zoom=4)
        m.add_heatmap(
        heritage,
        latitude="LATITUDE",
        longitude="LONGITUDE",
        value="AREAHA",
        name="Heat map",
        radius=20)
        m.to_streamlit(height=700)
    elif mode=='Default':
        m = leafmap.Map(
            center=[40, -100], zoom=4,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
        )
        m.add_geojson(regions, layer_name="Countries")
        m.add_points_from_xy(heritage,x="LONGITUDE",y="LATITUDE", popup=["NAME","DATEINSCRI","COUNTRY","DESCRIPTIO","AREAHA","DANGER","LONGITUDE","LATITUDE"])
        m.add_basemap(basemap)
        m.to_streamlit(height=700)
