import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("data.csv", low_memory=False, na_filter = False, encoding='latin-1', )

df.columns = df.columns.str.replace("ï»¿Opportunity Number","Opportunity Number")


st.set_page_config(layout="centered")

# Add the title
st.title("Dashboard Example")

# Sidebar

st.sidebar.header("Filter Here")


Sales_Team = st.sidebar.multiselect("Sales Team", options = df["Sales Team"].unique(),
default = df["Sales Team"].unique())

Pipeline_Category_Mgr = st.sidebar.multiselect("Pipeline Category Mgr", options = df["Pipeline Category Mgr"].unique(),
default = df["Pipeline Category Mgr"].unique())

Stage = st.sidebar.multiselect("Stage", options = df["Stage"].unique(),
default = df["Stage"].unique())

#Crear tu variable para que todo se seleccione de acuerdo a tus opciones de side bar
selected_options = df[(df["Sales Team"].isin(Sales_Team)) & (df["Pipeline Category Mgr"].isin(Pipeline_Category_Mgr)) & (df["Stage"].isin(Stage))]




chart = px.bar(selected_options, "Account Segmentation", "TCV", title="Acounnt Segmentation", color_discrete_sequence=["green"])

#do not display modebar
config = {'displayModeBar': False}
               
st.plotly_chart(chart, config=config)

chart2 = px.scatter(selected_options, "Account Segmentation", "TCV", title="Acounnt Segmentation", marker=dict(symbol="x"))

st.plotly_chart(chart2, config=config)

chart3 = px.bar(selected_options, "TCV", "Account Segmentation", title="Acounnt Segmentation", color_discrete_sequence=["pink"])
st.plotly_chart(chart3, config=config)

#Boton de Download
st.download_button("Download Data",selected_options.to_csv(), mime="text/csv")

#KPI
total_sales = int(selected_options["TCV"].sum())

