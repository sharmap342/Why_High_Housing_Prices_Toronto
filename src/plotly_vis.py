import plotly.express as px


#plot data using plotly 
def plotly_fig(df, **kwargs):
    """makes a plotly choropleth map
    
    Parameters
    ----------
    df: dataframe, data that needs to be plotted
    **kwargs: keyword arguments for px.choropleth function
    
    Returns
    -------
    fig: plotly fig object"""

    fig = px.choropleth(df, **kwargs)                    
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

