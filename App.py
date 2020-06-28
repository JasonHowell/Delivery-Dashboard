# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:23:51 2020

@author: Administrator
"""
#########################################################################
#
#  The app file.
#
#########################################################################

import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True