
# import dash
# from dash import html, dcc, callback, Input, Output
# from dash.exceptions import PreventUpdate
# # import os
# # from os import path
# import numpy as np
# # import sys

# from snippet1 import df1


# # Packages Related to Dash
# import dash
# from jupyter_dash import JupyterDash

# # from jupyter_dash import JupyterDash
# # import dash_core_components as dcc
# from dash import dcc
# # import dash_table as dt
# from dash import html
 
# from dash.dependencies import Output, Input
# from dash.exceptions import PreventUpdate

# import plotly.express as px
# import plotly.graph_objs as go



# dash.register_page(__name__, path='/CostlyCuisine')

# layout = html.Div(children=[
#     html.H1(children='This is our Analytics page'),
# 	html.Div([
#     html.Table([
#        html.Thead(
#            html.Tr([
#     html.Th([
#         html.Span(id="Country", ),
#         html.Span("'s Costlier Cuisine"),
#     ])
#     ])
#        ),
#        html.Tbody([
#            html.Tr([
#                html.Td([
#                 html.Span(id="Costlier_cui")
#                ])
#            ])
           
#        ])
#     ])
#       ] ) 
    
#     ])


# @callback(
#     [
#         Output('Country', 'children'),
#         Output('Costlier_cui', 'children')
#     ]
# )
# def update_city_selected():
#     x = 'India'
#     if x == None:
#         raise PreventUpdate
    