import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import altair as alt

st.set_page_config(layout="wide")

st.title("Main")
data="https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/point.geojson"
heritage=gpd.read_file(data)
regions = "https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/main/world-administrative-boundaries.geojson"
data2="https://github.com/Mr-bob-kou/My_Respository/raw/main/World%20Heritage%20Counts.geojson"
Count=gpd.read_file(data2)
data3="https://raw.githubusercontent.com/Mr-bob-kou/My_Respository/refs/heads/main/point2.geojson"
heritage2=gpd.read_file(data3)
count10=Count.sort_values(by='count', ascending=False).head(10)
heritage_sort=heritage.sort_values(by='NAME', ascending=True)

options = list(leafmap.basemaps.keys())
index = options.index("FWS NWI Wetlands")
modes=["Default","Heat Map","Choropleth Map(Heritage Count)","Inscribed Date","Classification"]
modes1="Default"
opt=["See All"]+list(heritage_sort['NAME'])

legend_dict = {
    "0":'#FFFFFF',
    "0-10":'#D2E9FF',
    "10-20":'#ACD6FF',
    "20-30": '#46A3FF',
    "30-40": '#0066CC',
    "40+": '#003060',
}

def style_function(feature):
    count = feature['properties']['count']
    
    if count > 40:
        color = '#003060'
    elif count > 30:
        color = "#0066CC"
    elif count > 20:
        color = '#46A3FF'
    elif count > 10:
        color = '#ACD6FF'
    elif count > 0 :
        color = '#D2E9FF'
    else:
        color='#FFFFFF'
    
    return {
        'fillColor': color,
        'color':"black",
        'weight': 2,
        'fillOpacity': 1
    }
def chromap(datum,mp):
    mp.add_basemap(basemap)
    mp.add_geojson(datum,style_callback=style_function) 
    mp.add_legend(title="Heritage Counts", legend_dict=legend_dict,draggable=False,position="bottomright")
    return mp.to_streamlit(height=700)
def heatmap(datum,mp,lat,lon,val):
    mp.add_heatmap(
        datum,
        latitude=lat,
        longitude=lon,
        value=val,
        name="Heat map",
        radius=20)
    return mp.to_streamlit(height=700)
def Default(datum,mp,lon,lat,pop):
    mp.add_geojson(regions, layer_name="Countries",zoom_to_layer=False)
    mp.add_points_from_xy(datum,x=lon,y=lat, popup=pop)
    mp.add_basemap(basemap)
    return mp.to_streamlit(height=700)

def to_df(datum,val):
    couda=datum.groupby(val).size()
    couda.to_frame()
    return couda.reset_index()
def cuml(datum,val):
    datum['aggr']=0
    for i in datum.index:
        if i==0:
            datum['aggr'][i]=datum[val][i]
        else:
            datum['aggr'][i]=datum[val][i]+datum['aggr'][i-1]
    return datum
def Info(NAME,COUNTRY,DESC):
    st.write("INFO:")
    st.write("Heritage Name:",NAME)
    st.write("Country:",COUNTRY)
    st.write("Description:",DESC)


with st.expander("See All Heritage Data"):
    st.dataframe(data=heritage, use_container_width=True)
col1, col2 = st.columns([4, 1])
with col2:
    basemap = st.selectbox("Select a basemap:", options, index)
    mode=st.selectbox("Select a Mode",modes)
    if mode=='Choropleth Map(Heritage Count)':
        chbox=st.checkbox("3-D Presentation")
        if chbox:
            st.write("Coming Soon")
    if mode=="Inscribed Date":
        Dateint=heritage['DATEINSCRI'].min()
        Dateend=heritage['DATEINSCRI'].max()
        Inscdate=st.slider("Choose the Year",Dateint,Dateend)
        st.write(Inscdate)
    if mode=="Default":
        place=st.selectbox("Choose a Place",opt)
        s=heritage[heritage['NAME']==place]
        if place=="See All":
            Info("NA","NA","NA")
        else:
            s=heritage[heritage['NAME']==place]
            h_name=s['NAME'].to_string(index=False)
            h_country=s['COUNTRY'].to_string(index=False)
            h_des=s['DESCRIPTIO'].to_string(index=False)
            Info(h_name,h_country,h_des)
with col1:
    m = leafmap.Map(center=[40, -100], zoom=4)
    if mode=='Choropleth Map(Heritage Count)':
        chromap(data2,m)
        st.write("#### Heritage Count Statistics(Top 10)")
        col3,col4,col5=st.columns([2,1,1])
        with col3:
            charts = alt.Chart(count10).mark_bar(size=20).encode(x=alt.X("name",type="nominal").sort("y"),y=alt.Y("count",type="quantitative"))
            st.altair_chart(charts,use_container_width=True)
            
    elif mode=='Heat Map':
       heatmap(heritage2,m,"LATITUDE","LONGITUDE","AREAHA")
        
    elif mode=='Default':
        if place=='See All':
            m1 = leafmap.Map(center=[40, -100], zoom=4,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            pop=["NAME","DATEINSCRI","COUNTRY","DESCRIPTIO","AREAHA","DANGER","LONGITUDE","LATITUDE"]
            Default(heritage,m1, "LONGITUDE","LATITUDE",pop)
        else:
            lat=s['LATITUDE'].to_string(index=False)
            long=s['LONGITUDE'].to_string(index=False)
            centers=[lat,long]
            m7 = leafmap.Map(center=centers,zoom=15,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            pop=["NAME","DATEINSCRI","COUNTRY","DESCRIPTIO","AREAHA","DANGER","LONGITUDE","LATITUDE"]
            Default(heritage,m7, "LONGITUDE","LATITUDE",pop)
        
        
    elif mode=="Inscribed Date":
        m=leafmap.Map(center=[40, -100], zoom=4)
        Insc=heritage[heritage['DATEINSCRI']==Inscdate]
        m.add_geojson(regions, layer_name="Countries")
        m.add_points_from_xy(Insc,x="LONGITUDE",y="LATITUDE", popup=["NAME","DATEINSCRI","COUNTRY","DESCRIPTIO","AREAHA","DANGER","LONGITUDE","LATITUDE"])
        m.add_basemap(basemap)
        m.to_streamlit(height=700)
        col3,col4=st.columns([3,1])
        with col4:
            chart_mode=['Line Chart','Bar Chart','Cumulative Line Chart']
            Chart_mode=st.selectbox("Select a Mode",chart_mode)
            years=to_df(heritage,'DATEINSCRI')
            years['aggr']=0
            years.rename(columns={0:'count'},inplace=True)
            pp=years[years['DATEINSCRI']==Inscdate]
            d=pp['count'].to_list()[0]
            st.write("Year:",Inscdate)
            st.write("Total:",d)
        with col3:
            cuml(years, 'count')
            cond=alt.condition(alt.datum.DATEINSCRI==Inscdate,alt.value('red'),alt.value('steelblue'))
            charts1 = alt.Chart(years).mark_line().encode(x=alt.X("DATEINSCRI",type='temporal'),y=alt.Y("count",type="quantitative"))
            charts2 = alt.Chart(years).mark_bar(size=10).encode(x=alt.X("DATEINSCRI",type='temporal'),y=alt.Y("count",type="quantitative"),color=cond)
            charts3= alt.Chart(years).mark_line().encode(x=alt.X("DATEINSCRI",type='temporal'),y=alt.Y("aggr",type="quantitative"))
            if Chart_mode=='Line Chart':
                st.altair_chart(charts1,use_container_width=True)
            if Chart_mode=='Bar Chart':
                st.altair_chart(charts2,use_container_width=True)
            if Chart_mode=='Cumulative Line Chart':
                st.altair_chart(charts3,use_container_width=True)

