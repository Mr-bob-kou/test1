import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")
data="https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/point.geojson"
heritage=gpd.read_file(data)
with st.expander("See All Heritage Data"):
    st.dataframe(data=heritage)

m = leafmap.Map(center=[40, -100], zoom=4)
regions = "https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/world-administrative-boundaries.geojson"

m.add_geojson(regions, layer_name="Countries")
m.add_points_from_xy(heritage,x="LONGITUDE",y="LATITUDE")

m.to_streamlit(height=700)
