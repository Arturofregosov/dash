import streamlit as st
import pandas as pd
import plotly.express as px
#Reading the Data
df = pd.read_csv("data.csv", low_memory=False, na_filter = False, encoding='latin-1', )
df.columns = df.columns.str.replace("ï»¿Opportunity Number","Opportunity Number")
st.set_page_config(page_title="Dashboard", layout="centered")


#Columns
 
col1, col2, col3 = st.columns(3)

with col1:
   st.text(df["TCV"].sum())
  

with col2:
   st.text("Text")
   

with col3:
   st.header("An owl")
 
st.markdown("""---""")

   # Side Bars
Sales_Team = st.sidebar.multiselect("Sales Team", options = df["Sales Team"].unique(),
default = df["Sales Team"].unique())

Pipeline_Category_Mgr = st.sidebar.multiselect("Pipeline Category Mgr", options = df["Pipeline Category Mgr"].unique(),
default = df["Pipeline Category Mgr"].unique())

Stage = st.sidebar.multiselect("Stage", options = df["Stage"].unique(),
default = df["Stage"].unique())

#Selected Options
selected_options = df[(df["Sales Team"].isin(Sales_Team)) & (df["Pipeline Category Mgr"].isin(Pipeline_Category_Mgr)) & (df["Stage"].isin(Stage))]

# Do not Display the Modebar
config = {'displayModeBar': False}

#Charts
chart = px.bar(selected_options, "Account Segmentation", "TCV", title="Acounnt Segmentation")
st.plotly_chart(chart, config=config)
chart2 = px.bar(selected_options, "TCV", "Account Segmentation", title="Acounnt Segmentation", color_discrete_sequence =['green'])
st.plotly_chart(chart2, config=config)

#Columns
 
col1, col2, col3 = st.columns(3)

with col1:
   st.text(selected_options["TCV"].sum())
  

with col2:
   st.text("Text")
   

with col3:
   st.header("An owl")
