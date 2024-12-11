import altair as alt
import pandas as pd

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
