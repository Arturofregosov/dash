import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard1",
    layout="centered"
)
st.header('Dashboard')

# Create some sample data
df = pd.read_csv("Data.csv", low_memory=False, na_filter = False, encoding='latin-1', )

# Download Button
st.download_button("Download Data",df.to_csv(), mime="text/csv")

# Columns
col1,col2,col3 = st.columns(3)
col1.metric("lo que sea","lo que sea", "lo que sea")
col2.metric("lo que sea","lo que sea", "lo que sea")
col3.metric("lo que sea","lo que sea", "lo que sea")

# Create a multiselect widget to select the data series to display
selected_series = st.multiselect("",df['Fy Qtr'].unique(), default=["FY2023-Q2"])

# Create a plotly chart of the selected data series
chart = px.bar(df[df['Fy Qtr'].isin(selected_series)], x='Account Name', y='TCV', hover_data={'TCV':':$,.0f'},  color_discrete_sequence =['green'])
chart2 = px.line(df[df['Fy Qtr'].isin(selected_series)], x='Account Name', y='TCV', hover_data={'TCV':':$,.0f'}, color_discrete_sequence =['red'])
st.plotly_chart(chart, config={'displayModeBar': False})
st.plotly_chart(chart2, config={'displayModeBar': False})

















