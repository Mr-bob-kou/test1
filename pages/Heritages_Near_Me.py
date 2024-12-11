import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import altair as alt

st.set_page_config(layout="wide")


st.title("Heritage Near Me")
data="https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/point.geojson"
heritage=gpd.read_file(data)
regions = "https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/world-administrative-boundaries.geojson"
mp = leafmap.Map(center=[40, -100], zoom=4,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
pop=["NAME","DATEINSCRI","COUNTRY","DESCRIPTIO","AREAHA","DANGER","LONGITUDE","LATITUDE"]
mp.add_geojson(regions, layer_name="Countries")
mp.add_points_from_xy(heritage,x="LONGITUDE",y="LATITUDE", popup=pop)
mp.add_basemap(basemap)
mp.to_streamlit(height=700)
