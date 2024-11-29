import streamlit as st
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

data1="https://github.com/Mr-bob-kou/My_Respository/raw/main/World%20Heritage%20Counts.geojson"
st.title("Marker Cluster")
gdf = gpd.read_file(data1)
st.dataframe(data=gdf)
