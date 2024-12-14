import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import altair as alt

st.set_page_config(layout="wide")


st.title("Adding!!")
st.write("Coming Soon......")
with st.form("my_form"):
    st.write("Inside the form")
    name = st.text_input("Name")
    Country= st.text_input("Country")

    submitted = st.form_submit_button("Submit")
if submitted:
    st.write("Name", name, "Country", country)
