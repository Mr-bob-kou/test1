import altair as alt
import pandas as pd
import streamlit as st

# 創建範例數據
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 30, 50, 20, 60]
})

# 使用條件語句來設置顏色
chart = alt.Chart(data).mark_bar().encode(
    x='category',
    y='value',
    color=alt.condition(
        alt.datum.value > 40,  # 如果 value 大於 40，則應用紅色
        alt.value('red'),      # 這是條件為真時的顏色
        alt.value('steelblue') # 這是條件為假時的顏色
    )
)


st.altair_chart(chart,use_container_width=True)

data = pd.DataFrame({
    'time': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'value': [10, 20, 30, 25, 15]
})

data['time'] = pd.to_datetime(data['time'])

highlight_time_range = ['2024-01-02', '2024-01-04']

chart1 = alt.Chart(data).mark_bar().encode(
    x='time:T',  # T 表示時間類型
    y='value:Q',  # Q 表示數值型
    color=alt.condition(
        alt.FieldOneOfPredicate(field='time', oneOf=highlight_time_range),  # 如果時間在特定範圍內
        alt.value('red'),  # 高亮顯示的顏色
        alt.value('steelblue')  # 默認顏色
    )
)
st.altair_chart(chart1,use_container_width=True)
