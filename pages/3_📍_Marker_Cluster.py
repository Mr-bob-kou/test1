import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")


st.title("General")
data="https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/point.geojson"
regions = "https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/world-administrative-boundaries.geojson"
heritage=gpd.read_file(data)
with st.expander("See All Heritage Data"):
    st.dataframe(data=heritage)
col1, col2 = st.columns([4, 1])
with col2:
    st.write("Blank Space")
with col1:
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_geojson(regions, layer_name="Countries")
    m.add_points_from_xy(heritage,x="LONGITUDE",y="LATITUDE", popup=["NAME","DATEINSCRI","COUNTRY","DESCRIPTIO","AREAHA","DANGER","LONGITUDE","LATITUDE"])
    m.to_streamlit(height=700)
