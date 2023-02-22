import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from dataEngineering import dataEngineering
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

app = JupyterDash(__name__, use_pages=True)
# app = JupyterDash(__name__)

app.layout = html.Div([

    html.Div(
        [
            
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"], style={"font-size":"1.2rem","display": "inline","position": 'relative','padding': "5px", "text-decoration": "none", 'top': '10px','color':'white', 'border': '2px solid green' ,'background-color':'green', 'margin':'20px', 'padding':'10px'}
		            
                )
            for page in dash.page_registry.values()
        ]
    ),

	     dash.page_container
])

# Inside html.Div
# dcc.Link(
#                     f"{page['name']} - {page['path']}", href=page["relative_path"]
#                 )

# Just after html.Div Ends and before square brace
# for page in dash.page_registry.values()

# before the last square brace
# dash.page_container


if __name__ == '__main__':
	app.run_server(debug=True)