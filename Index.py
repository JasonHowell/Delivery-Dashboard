# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:24:34 2020

@author: Administrator
"""

##########################################################################
#
# COGS Delivery Dashboard 
#
# Gives a quick overview of the Programmes lifecycle stages
#
# Driven from the index page each tab runs in it's own right.  
#
#
##########################################################################


import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from App import app
import Tab_1
import Tab_2
import Tab_3
import Tab_4
import Tab_5
import Tab_6


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


#############################################################################
#
# This defines the overall structure of the dashboard.  It calls each 
# component as a tab-n file.  Each Tab-n file is mini dash board in its
# own right.
#############################################################################

app.layout = html.Div([
    html.Div(
        html.H1('COGS Delivery Dashboard.  5* Open Data Programme, ONS', style={
            'textAlign': 'center',
            'color': colors['text']
        })
    ),
#        html.H3('5* Open Data Programme, ONS', style={
#            'textAlign': 'center',
#            'color': colors['text']
#           }),
        
    dcc.Tabs(id="tabs", value='tab-1', children=[
#        dcc.Tab(label='PMDv3 Datasets Tab_1', id='Tab_1' value='Tab_1'),
        dcc.Tab(label='PMDv3 Datasets', id='Tab_1', value='tab-1'),
        dcc.Tab(label='PMDv4 Datasets', id='Tab_2', value='tab-2'),
        dcc.Tab(label='BA Airtable Profile', id='Tab_3', value='tab-3'),
        dcc.Tab(label='Swirrl Github Repo', id='Tab_4', value='tab-4'),
        dcc.Tab(label='OneTech Team Github Repo', id='Tab_5', value='tab-5'),
        dcc.Tab(label='E2E Defect Profile', id='Tab_6', value='tab-6'),
        ]),
   html.Div(id='tabs-output')
])

############################################################################
#
#  This is the callback element which actually calls the tab file based
#  on the value property.
#
###########################################################################

@app.callback(
        Output('tabs-output', 'children'),
              [Input('tabs', 'value')])
#def render_content(tab):
def show_content(value):
    if value == 'tab-1':  
        return html.Div([Tab_1.Tab_1_layout])
    elif value == 'tab-2':
        return html.Div([Tab_2.Tab_2_layout])
    elif value == 'tab-3':
        return html.Div([Tab_3.Tab_3_layout])
    elif value == 'tab-4':
        return html.Div([Tab_4.Tab_4_layout])
    elif value == 'tab-5':
        return html.Div([Tab_5.Tab_5_layout])
    elif value == 'tab-6':  
        return html.Div([Tab_6.Tab_6_layout])
    else:
        html.Div()

##########################################################################
#        
#  This actuall starts the webserver.  Currently debug set to "True"
#
##########################################################################
    
if __name__ == '__main__':
    app.run_server(debug=True)