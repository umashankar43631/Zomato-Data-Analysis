import dash
from dash import html, dcc, callback, Input, Output
from dash.exceptions import PreventUpdate
from plotly.subplots import make_subplots

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

def get_avg_rating(filtered_df):
    sum_of_ratings = 0
    for i in filtered_df.index:
        sum_of_ratings += filtered_df.iloc[i]['rating_num']
    length_of_df = len(filtered_df)
    if(sum_of_ratings// length_of_df >= 3):
        return "Excellent - 5.0 "
    elif(sum_of_ratings// length_of_df >= 2):
        return "Very Good - 4.5 "
    elif(sum_of_ratings// length_of_df >= 1):
        return "Good - 4.0"
    elif(sum_of_ratings// length_of_df >= 0):
        return "Average - 3.5"
    else:
        return "Poor - 3.0"
    
    

dash.register_page(__name__, path='/')
fig = make_subplots(rows=1, cols=2)

layout = html.Div([
   
   html.H1('Data Analysis'),

   html.Div([
    html.Table(children = [
       html.Thead(
           html.Tr([
                        html.Th([
                            
                            html.Span(id="Country_id" ),
                            html.Span("'s Costlier Cuisine"),
                                ], 
                        style={      
                               'border': '2px solid black', 'padding': '3px', 'margin': '5px'
                            }
                                ),

                        html.Th([
                            
                            html.Span(id="Country_id1" ),
                            html.Span("'s Cuisine's Rating"),
                                ], 
                        style={      
                               'border': '2px solid black', 'padding': '3px', 'margin': '5px'
                            }
                                )

                ])
       ),
       html.Tbody([
           html.Tr([
               html.Td([
                html.Span(id = 'costlier_cuisines')
               ]
                   ,
           style={      
                    'border': '2px solid orange', 'text-align': 'center' ,'padding': '3px', 'margin': '5px', 'color': 'orange', 'background-color':'black'
                    }               
               ),
             html.Td([
                html.Span(id = 'rating_cuisines')
               ]
                   ,
           style={      
                    'border': '2px solid #c44dff' ,'padding': '3px', 'text-align': 'center' , 'margin': '5px', 'color': '#3bed18', 'background-color':'black'
                    }               
               )

           ] 
           )
           
       ])
    ], style = { 'border': '2px solid black', 'padding': '3px', 'margin': '5px'
                         }
    
    )  ], style={'margin': '10px', 'padding': '5px', 'background-color':'silver', 'display': 'inline-block'} ),

   html.Div([
   dcc.Dropdown(id='data-dropdown', options=[
       {'label': country, 'value': country} 
       for country in df1['Country'].unique()], 
       placeholder= "Select Country", value='India')]),
    html.Br(),
    html.Br(),
    # html.Div(children= [
    # dcc.Graph(id="graph1"),
    #     dcc.Graph(id='graph2')
    
    # ]),

    # dcc.Graph(id='graph', style={'display': 'inline', 'float': 'left'}),
    # dcc.Graph(id='graph1', style={'display': 'inline', 'float': 'right'}),

  
    html.P([   
            
            dcc.Graph(id='graph'),            
            dcc.Graph(id='graph1'),

    ]),
    html.Br(),
    dcc.Graph(id='graph2', style={'display': 'block'}),
    



    html.Br(),
    html.Br(),
    html.Div([
    
    ]),
    html.Br(),
    html.Br(),
    # html.Div(children = [
    #     dcc.Graph(id='graph3', style={'display': 'block'})
    # ])
] )          



# @callback([
#     Output('Country_id', 'children'),
#     Output('Country_id1', 'children'),
#     Output('costlier_cuisines', 'children'),
#     Output('rating_cuisines', 'children'),
#     Output('graph1', 'figure'),
#     Output('graph2', 'figure'),
#     Output('graph3', 'figure')
# ],
#     Input('data-dropdown', 'value'))
@callback([
    Output('Country_id', 'children'),
    Output('Country_id1', 'children'),
    Output('costlier_cuisines', 'children'),
    Output('rating_cuisines', 'children'),
    Output('graph', 'figure'),
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),

],
    Input('data-dropdown', 'value'))
def task1(value):
    # if value is None:
    #     raise PreventUpdate
    filtered_df = df1[df1['Country']== value]
    fig = px.histogram(filtered_df, x='Country', width=350, color='Rating text')
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

    # Average rating of a city based on restaurants rating
    sum_of_ratings = 0
    j = 0
    for i in filtered_df.index:
        sum_of_ratings += (filtered_df.iloc[j]['rating_num'])
        j+=1
    length_of_df = len(filtered_df)
    if(sum_of_ratings// length_of_df >= 3):
        rating_cuisine =  "Excellent - 5.0 "
    elif(sum_of_ratings// length_of_df >= 2):
        rating_cuisine ="Very Good - 4.5 "
    elif(sum_of_ratings// length_of_df >= 1):
        rating_cuisine = "Good - 4.0"
    elif(sum_of_ratings// length_of_df >= 0):
        rating_cuisine = "Average - 3.5"
    else:
        rating_cuisine = "Poor - 3.0"

    # --------------------------------
    # Online vs Dine-in
    d3=filtered_df.groupby(["Has Online delivery"])['Has Online delivery'].count()

    fig2=px.pie(d3,names=['Dine-in', 'Online'], values=list(filtered_df['Has Online delivery'].value_counts()), title = "Online vs dine-in")
    
    # figure1 = go.Figure(data=[fig1])
    # figure2 = go.Figure(data=[fig2])
    # figure = go.Figure(data=[fig])
    # fig2 = px.pie(filtered_df, values='Has Online delivery', names='Has Online delivery')
    return value ,value, costlier_cuisine, rating_cuisine, fig,fig1, fig2
