import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv("data.csv", low_memory=False, na_filter = False, encoding='latin-1', )

df.columns = df.columns.str.replace("ï»¿Opportunity Number","Opportunity Number")


st.set_page_config(
    page_title="Dashboard", layout="centered"
)



# Sidebar
st.sidebar.header("Filter Here")

Sales_Team = st.sidebar.multiselect("Sales Team", options = df["Sales Team"].unique(),
default = df["Sales Team"].unique())

Pipeline_Category_Mgr = st.sidebar.multiselect("Pipeline Category Mgr", options = df["Pipeline Category Mgr"].unique(),
default = df["Pipeline Category Mgr"].unique())

Stage = st.sidebar.multiselect("Stage", options = df["Stage"].unique(),
default = df["Stage"].unique())


selected_options = df[(df["Sales Team"].isin(Sales_Team)) & (df["Pipeline Category Mgr"].isin(Pipeline_Category_Mgr)) & (df["Stage"].isin(Stage))]


chart = px.bar(selected_options, "Account Segmentation", "TCV", title="Acounnt Segmentation", hover_data={'TCV':':$,.2f'})
chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)
chart.update_traces(marker_color='pink')
config = {'displayModeBar': False}


st.plotly_chart(chart, config=config)
