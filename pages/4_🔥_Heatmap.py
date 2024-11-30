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

st.title("Heatmap")
data="https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/point.geojson"
heritage=gpd.read_file(data)
with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[40, -100], zoom=4)
        m.add_heatmap(
            heritage,
            latitude="LATITUDE",
            longitude="LONGITUDE",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
