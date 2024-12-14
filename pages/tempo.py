import streamlit as st
import leafmap.foliumap as leafmap
import folium
from folium import GeoJson
import geopandas as gpd
data="/content/drive/MyDrive/113-1_GIS_programing/data/worldheritagesites.shp"
heritage=gpd.read_file(data)
place="Minaret and Archaeological Remains of Jam"
d=heritage[heritage['NAME']==place]
lat=d['LATITUDE'].to_string(index=False)
long=d['LONGITUDE'].to_string(index=False)
centers=[lat,long]
m = leafmap.Map(center=centers, zoom=17)
regions = "https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/world-administrative-boundaries.geojson"
output_file = "point.geojson"
heritage.to_file(output_file, driver="GeoJSON")
s=heritage.sort_values(by='NAME', ascending=True)
m.add_geojson(regions, layer_name="US Regions")
m.add_points_from_xy(heritage,x="LONGITUDE",y="LATITUDE",popup=["NAME","DATEINSCRI","COUNTRY","DESCRIPTIO","AREAHA"],marker_colors=['red'],spin=True)
m.to_streamlit(width=700)
