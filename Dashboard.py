import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(page_title="Dashboard AFV", layout="centered")

@st.cache
def get_data():
    df = pd.read_csv("data.csv", low_memory=False, na_filter=False, encoding='latin-1')
    df.columns = df.columns.str.replace("├»┬╗┬┐Opportunity Number","Opportunity Number")
    return df
df = get_data()

# Sidebar
Sales_Team = st.sidebar.multiselect("Sales Team", options = df["Sales Team"].unique(),
default = df["Sales Team"].unique())

Pipeline_Category_Mgr = st.sidebar.multiselect("Pipeline Category Mgr", options = df["Pipeline Category Mgr"].unique(),
default = df["Pipeline Category Mgr"].unique())

Stage = st.sidebar.multiselect("Stage", options = df["Stage"].unique(),
default = df["Stage"].unique())

#Connect all the sidebars ao they filter on the selection
selected_options = df[(df["Sales Team"].isin(Sales_Team)) & (df["Pipeline Category Mgr"].isin(Pipeline_Category_Mgr)) & (df["Stage"].isin(Stage))]

# Calculate sum and count of selected options
total_sum = selected_options["TCV"].sum()
total_count = selected_options.shape[0]

#Columns
col1, col2 = st.columns(2)
col1.write(f"Total Sum: ${total_sum:,.2f}")
col2.write(f"Total Count: {total_count}")

#Do not display mode bar variable
config = {'displayModeBar': False}

#Chart
chart = px.bar(selected_options, "Account Segmentation", "TCV", title="Chart 1", hover_data={'TCV':':$,.2f'})
chart.update_layout(yaxis_title=None)
chart.update_layout(xaxis_title=None)
chart.update_layout(plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
chart.update_traces(marker_color='light blue')
st.plotly_chart(chart, config=config)

#Chart2
chart2 = px.bar(selected_options, "TCV", "Account Segmentation", title="Chart 2", hover_data={'TCV':':$,.2f'})
chart2.update_layout(yaxis_title=None)
chart2.update_layout(xaxis_title=None)
chart2.update_layout(plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
chart2.update_traces(marker_color='purple')
st.plotly_chart(chart2, config=config)

#Hide Style
hide_style = """<style> 
                #MainMenu {visibility:hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_style, unsafe_allow_html=True)

