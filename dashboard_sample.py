import streamlit as st
import pandas as pd
import plotly.express as px
#Reading the Data
df = pd.read_csv("data.csv", low_memory=False, na_filter = False, encoding='latin-1', )
df.columns = df.columns.str.replace("ï»¿Opportunity Number","Opportunity Number")
#Page Config
#st.set_page_config(page_title="Dashboard", layout="wide")
# Title
st.header("Dashboard") 
#Division
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

# Do not Display the Modebar Variable
config = {'displayModeBar': False}

#Total
#st.write("Total Value "+"{:,}".format(int(selected_options["TCV"].sum())))
st.beta_columns([
    ("Left Column Title", st.write("Total Value "+"{:,}".format(int(selected_options["TCV"].sum())))),
    ("Right Column Title", st.write("Total Value "+"{:,}".format(int(selected_options["TCV"].sum())))),
])

#Charts
chart = px.bar(selected_options, "Account Segmentation", "TCV", title="Acounnt Segmentation", hover_data={'TCV':':$,.0f'})
st.plotly_chart(chart, config=config)
chart2 = px.bar(selected_options, "TCV", "Account Segmentation", title="Acounnt Segmentation", color_discrete_sequence =['green'], hover_data={'TCV':':$,.0f'})
st.plotly_chart(chart2, config=config)
  
  

