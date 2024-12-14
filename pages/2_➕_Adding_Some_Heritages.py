import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import altair as alt

st.set_page_config(layout="wide")


st.title("Adding!!")
st.write("Coming Soon......")
yr_range=list(range(1900,2100))
with st.form("my_form"):
    st.write("Inside the form")
    name = st.text_input("Name")
    country= st.text_input("Country")
    year=st.selectbox("Inscribed Year",yr_range)
    description=st.text_area("Description","NA")

    submitted = st.form_submit_button("Submit")
if submitted:
    st.write("Name", name, "Country", country)
    st.write("Year",year)
    st.write("description",description)
