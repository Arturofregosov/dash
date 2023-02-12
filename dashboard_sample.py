import streamlit as st
import pandas as pd
import plotly.express as px

#--------------Reading the Data and caching the data
@st.cache
def get_data_from_csv():
    df = pd.read_csv("data.csv", low_memory=False, na_filter = False, encoding='latin-1', )
    return df
df = get_data_from_csv()
      
#-------------Replacing some strange values that datasource columns have
df.columns = df.columns.str.replace("ï»¿Opportunity Number","Opportunity Number")

#---------------title
st.title(":bar_chart: Dashboard")
#------------------------- header
#st.header(":bar_chart: Dashboard") 

#--------------------------Division-------------
st.markdown("""---""")

#---------------------- Sidebars-----------------

Sales_Team = st.sidebar.multiselect("Sales Team", options = df["Sales Team"].unique(),
default = df["Sales Team"].unique())

Pipeline_Category_Mgr = st.sidebar.multiselect("Pipeline Category Mgr", options = df["Pipeline Category Mgr"].unique(),
default = df["Pipeline Category Mgr"].unique())

Stage = st.sidebar.multiselect("Stage", options = df["Stage"].unique(),
default = df["Stage"].unique())

#------------------Selected Options
selected_options = df[(df["Sales Team"].isin(Sales_Team)) & (df["Pipeline Category Mgr"].isin(Pipeline_Category_Mgr)) & (df["Stage"].isin(Stage))]

# ---------------------Do not Display the Modebar Variable
config = {'displayModeBar': False}

#---------------------KPI Total Value and Total Count Variables
left_column, right_column = st.columns(2)

with left_column:
    st.write("Total Value  "+"${:,}".format(int(selected_options["TCV"].sum())))
    
with right_column:
    st.write("Total Count  "+"{:,}".format(int(selected_options["TCV"].count())))

#---------------------------------Charts-----------------------------------------
#Chart 1
chart = px.bar(selected_options, "Account Segmentation", "TCV", title="Acounnt Segmentation",color_discrete_sequence =['pink'],hover_data={'TCV':':$,.0f'})

chart = chart.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
})

st.plotly_chart(chart, config=config)

#Chart 2

chart2 = px.bar(selected_options, "TCV", "Account Segmentation", title="Acounnt Segmentation", color_discrete_sequence =['green'], hover_data={'TCV':':$,.0f'})

chart2 = chart2.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
})

st.plotly_chart(chart2, config=config)

#Chart 3

chart3 = px.pie(selected_options, values='TCV', names='Sales Team', title='Sales Team')

st.plotly_chart(chart3, config=config)
  
#------------------------------Hide Streamlit Style

hidestyle ="""
      <style>
      footer {visibility : hidden;}
      header {visibility : hidden;}
      </style>
      """
st.markdown(hidestyle, unsafe_allow_html=True)

