import streamlit as st
import pandas as pd
import plotly.express as px





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

st.dataframe(selected_options)

chart = px.bar(selected_options, "Account Segmentation", "TCV", title="Acounnt Segmentation")


config = {'displayModeBar': False}


st.plotly_chart(chart, config=config)

