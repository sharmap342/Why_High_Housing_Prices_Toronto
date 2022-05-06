import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import json
import plotly.express as px
from plotly_vis import plotly_fig #import plotly_fig function for data visualization
import data_dic


#import geojson file 
with open('../data/cleaned/toronto_district.geojson') as f:
    data_district = json.load(f)


def import_data(path, cols, **kwargs):
    """imports data in a dataframe
    
    Parameters
    ----------
    path: path where data is located
    cols: list of columns to be removed from columns
    kwargs: any parameters related ot pd.read_csv method
    
    Returns
    -------
    df: dataframe with imported data
    columns: list of columns in data without cols"""
    #import data
    df = pd.read_csv(path, **kwargs)
    columns = df.columns.to_list()
    #remove columns listed in cols from columns list
    for col in cols:
        columns.remove(col)

    return (df, columns)

#set title 
st.title('Visualizing Housing Prices in Toronto')

#Ask user to provide a parameters  
parameters = st.selectbox('Select the parameters to be plotted', ('Actual', 'Benchmark'))

#ask user for variables 
if parameters == 'Actual':
    df, columns = import_data('../data/cleaned/district_price.csv',
                                ['Name', 'month', 'day', 'year', 'date'],
                                index_col=0)
    parameter = st.selectbox('Select the variable to be plotted', tuple(columns))
else: 
    df, columns = import_data('../data/cleaned/district_MLS.csv',
                                ['Name', 'month', 'day', 'year', 'date'],
                                index_col=0)
    parameter = st.selectbox('Select the variable to be plotted', tuple(columns))


#plot the variables
fig = plotly_fig(df, geojson=data_district, color=parameter,
                    locations="Name", featureidkey="properties.District",
                    projection="mercator", animation_frame='date',
                    color_continuous_scale=px.colors.sequential.RdPu)
st.markdown("<h2 style='text-align: center; color: grey;'>Toronto Housing Market over Time</h2>",
            unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown(f'*** {parameter} - {data_dic.data_description[parameter]}')
