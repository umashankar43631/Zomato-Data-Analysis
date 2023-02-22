import dash
from dash import html, dcc, callback, Input, Output
from dash.exceptions import PreventUpdate
# import os
# from os import path
import numpy as np
# import sys

from snippet1 import df1


# Packages Related to Dash
import dash
from jupyter_dash import JupyterDash

# from jupyter_dash import JupyterDash
# import dash_core_components as dcc
from dash import dcc
# import dash_table as dt
from dash import html
 
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

import plotly.express as px
import plotly.graph_objs as go


# current = os.path.dirname(os.path.realpath(__file__))
# # parent1 = os.path.dirname(x)
# parent = os.path.dirname(current)
# sys.path.append(parent)


def values_gt_mean(d2):
    d3 = {}
    avg_value = np.mean(list(d2.values()))
    for i, j in d2.items():
        if j>= avg_value:
            d3[i] = j
    return d3 

dash.register_page(__name__, path='/')

layout = html.Div([
   
   html.H1('Data Analysis'),

   html.Div([
    html.Table(children = [
       html.Thead(
           html.Tr([
    html.Th([
        html.Span(id="Country_id" ),
        html.Span("'s Costlier Cuisine"),
    ])
    ])
       ),
       html.Tbody([
           html.Tr([
               html.Td([
                html.Span(id = 'costlier_cuisine')
               ])
           ])
           
       ])
    ]
    
    )  ], style={'margin': '10px', 'padding': '5px', 'background-color':'silver', 'display': 'inline-block'} ),

   html.Div([
   dcc.Dropdown(id='data-dropdown', options=[
       {'label': country, 'value': country} 
       for country in df1['Country'].unique()], 
       placeholder= "Select Country", value='India')]),
    html.Br(),
    html.Br(),
    html.Div(children= [
    dcc.Graph(id="fig"),
    dcc.Graph(id='fig1')
    ])
] )          



@callback([
    Output('Country_id', 'children'),
    Output('costlier_cuisine', 'children'),
    Output('fig', 'figure'),
    Output('fig1', 'figure'),
    Output('fig', 'style'),
    Output('fig1', 'style')
],
    Input('data-dropdown', 'value'))
def task1(value):
    if value is None:
        raise PreventUpdate
    filtered_df = df1[df1['Country']== value]
    fig = px.histogram(filtered_df, x='Country', width=350)
    fig.update_layout(
        title=f"{value} restaurants count",
        xaxis_title="Country",
        yaxis_title="Restaurants count",
        legend_title="country count plot"
    )
    cui_count = {}
    for cuisi in filtered_df['Cuisines']:
        for cuis in str(cuisi).split(','):
            if (cuis== '' or cuis==' '):
                continue
            cuis = cuis.strip()
            if cuis in cui_count:
                cui_count[cuis] += 1
            else:
                cui_count[cuis] = 1
    cui_count_avg = values_gt_mean(cui_count)
    cui_count_avg = dict(sorted(cui_count_avg.items(), key=lambda x: x[1], reverse=True))
    fig1 = px.bar(x = list(cui_count_avg.keys()), y=list(cui_count_avg.values()), width=900, labels = list(cui_count_avg.keys()), title="Favourite Cousin")
    
    fig1.update_layout(
        title=f"{value} Favourite Cuisines",
        xaxis_title="Cuisines",
        yaxis_title="count",
        legend_title=f"Favourite Cuisines {value}",
    )
    graph1_style = {
        'display': 'inline',
        'float': 'left'
    }
    graph2_style = {
        'display': 'inline',
        'float': 'left'
    }

    costlier_cuisine = filtered_df[filtered_df['rupees']== max(filtered_df['rupees'])]['Cuisines'].astype('str')
    costlier_cuisine = ''.join(costlier_cuisine.unique())
    
    return value, costlier_cuisine, fig, fig1,graph1_style, graph2_style
